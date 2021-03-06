$(function() {
    StagingViewModel = {

        available_icds_neoplasms: ko.observableArray([]),
        available_icds: ko.observableArray([]),
        available_ts:  ko.observableArray([]),
        available_ns:  ko.observableArray([]),
        available_ms:  ko.observableArray([]),
        available_dukes: ko.observableArray([]),
        available_psa: ko.observableArray([]),
        available_gleason: ko.observableArray([]),

        current_icds_neoplasm: ko.observable(''),
        current_icd: ko.observable(''),
        current_t:  ko.observable(''),
        current_n:  ko.observable(''),
        current_m:  ko.observable(''),
        current_dukes: ko.observable(''),
        current_psa: ko.observable(''),
        current_gleason: ko.observable(''),

        calculated_stage: ko.observable(''),

        loadInitialState: function () {
            $('#l_dukes').hide()
            $('#dukes_selector').hide();
            $('#l_psa').hide()
            $('#psa_selector').hide();
            $('#l_gleason').hide()
            $('#gleason_selector').hide();
            $('#b_stage').hide();
            $.getJSON('get_icds', function (json) {
                StagingViewModel.available_icds(json.icd_list);
                //StagingViewModel.available_icds_neoplasms(json.icd_list_neoplasm);
            });
        },

        icdChanged: function () {
            console.log(StagingViewModel.current_icd());
            $('#b_stage').hide();
            StagingViewModel.available_ts([]);
            StagingViewModel.available_ns([]);
            StagingViewModel.available_ms([]);
            StagingViewModel.available_dukes([]);
            StagingViewModel.available_psa([]);
            StagingViewModel.available_gleason([]);
            StagingViewModel.calculated_stage('');


            if(StagingViewModel.current_icd() === 'C18 - Colorectal - Colon' ||
                StagingViewModel.current_icd() === 'C19 - Colorectal - Rectosigmoid' ||
                StagingViewModel.current_icd() === 'C20 - Colorectal - Rectum'){
                $('#l_dukes').show()
                $('#dukes_selector').show();
            }
            else{
                $('#l_dukes').hide()
                $('#dukes_selector').hide();
            }

            if(StagingViewModel.current_icd() === 'C61 - Prostate'){

                $('#l_psa').show();
                $('#psa_selector').show();
                $('#l_gleason').show();
                $('#gleason_selector').show();
            }
            else{
                $('#l_psa').hide();
                $('#psa_selector').hide();
                $('#l_gleason').hide();
                $('#gleason_selector').hide();
            }

            $.getJSON('get_tnms/' + StagingViewModel.current_icd(), function (json) {

                StagingViewModel.available_ts(json.ts_list);
                StagingViewModel.available_ns(json.ns_list);
                StagingViewModel.available_ms(json.ms_list);
                StagingViewModel.available_dukes(json.dukes_list);
                StagingViewModel.available_psa(json.psa_list);
                StagingViewModel.available_gleason(json.gleason_list);

            });
            },

        tnmChanged:function() {
            if (StagingViewModel.current_icd() === 'C18 - Colorectal - Colon' ||
                StagingViewModel.current_icd() === 'C19 - Colorectal - Rectosigmoid' ||
                StagingViewModel.current_icd() === 'C20 - Colorectal - Rectum') {
                if (StagingViewModel.current_t() !== undefined &&
                StagingViewModel.current_n() !== undefined &&
                StagingViewModel.current_m() !== undefined &&
                StagingViewModel.current_dukes() !== undefined) {

                $.getJSON('get_stage/' + StagingViewModel.current_icd() + '/' + StagingViewModel.current_t() + '/' +
                    StagingViewModel.current_n() + '/' + StagingViewModel.current_m() +
                    '/' + StagingViewModel.current_dukes() + '/'+
                    StagingViewModel.current_psa() + '/' + StagingViewModel.current_gleason(), function (json) {
                    StagingViewModel.calculated_stage(json.stage);
                    $('#b_stage').show();
                    });
                }//fim if interno


            }//fim if C18
            else if (StagingViewModel.current_icd() === 'C61 - Prostate') {
                if (StagingViewModel.current_t() !== undefined &&
                StagingViewModel.current_n() !== undefined &&
                StagingViewModel.current_m() !== undefined &&
                StagingViewModel.current_psa() !== undefined &&
                StagingViewModel.current_gleason() !== undefined) {

                $.getJSON('get_stage/' + StagingViewModel.current_icd() + '/' + StagingViewModel.current_t() + '/' +
                    StagingViewModel.current_n() + '/' + StagingViewModel.current_m() +
                    '/' + StagingViewModel.current_dukes() + '/'+
                    StagingViewModel.current_psa() + '/' + StagingViewModel.current_gleason(), function (json) {
                    $('#b_stage').show();
                    StagingViewModel.calculated_stage(json.stage);
                    });
                }//fim if interno

            }//fim if C61
            else {

            // resto CID
            if (StagingViewModel.current_icd() !== undefined &&
                StagingViewModel.current_t() !== undefined &&
                StagingViewModel.current_n() !== undefined &&
                StagingViewModel.current_m() !== undefined) {

                $.getJSON('get_stage/' + StagingViewModel.current_icd() + '/' + StagingViewModel.current_t() + '/' +
                    StagingViewModel.current_n() + '/' + StagingViewModel.current_m() +
                    '/' + StagingViewModel.current_dukes() + '/' +
                    StagingViewModel.current_psa() + '/' + StagingViewModel.current_gleason(), function (json) {
                    $('#b_stage').show();
                    StagingViewModel.calculated_stage(json.stage);
                });
            }//fim if interno
            }// fim if resto CID


        }
    };

    ko.applyBindings(StagingViewModel);
    StagingViewModel.loadInitialState();
});
