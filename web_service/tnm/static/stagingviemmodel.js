$(function() {
    StagingViewModel = {

        available_icd_neoplasms: ko.observableArray([]),
        available_icds: ko.observableArray([]),
        available_ts:  ko.observableArray([]),
        available_ns:  ko.observableArray([]),
        available_ms:  ko.observableArray([]),
        available_dukes: ko.observableArray([]),
        available_psa: ko.observableArray([]),
        available_gleason: ko.observableArray([]),

        current_icd_neoplasm: ko.observable(''),
        current_icd: ko.observable(''),
        current_t:  ko.observable(''),
        current_n:  ko.observable(''),
        current_m:  ko.observable(''),
        current_dukes: ko.observable(''),
        current_psa: ko.observable(''),
        current_gleason: ko.observable(''),

        calculated_stage: ko.observable(''),

        loadInitialState: function () {
            $('#dukes_selector').hide();
            $('#psa_selector').hide();
            $('#gleason_selector').hide();
            $.getJSON('get_icds_neoplasm', function (json) {
                //StagingViewModel.available_icds(json.icd_list);
                StagingViewModel.available_icd_neoplasms(json.icd_list_neoplasm);
            });
        },

        icdChanged: function () {
            StagingViewModel.available_ts([]);
            StagingViewModel.available_ns([]);
            StagingViewModel.available_ms([]);
            StagingViewModel.calculated_stage('');

            //if(StagingViewModel.current_icd() === 'C18' ||
            //    StagingViewModel.current_icd() === 'C19' ||
            //    StagingViewModel.current_icd() === 'C20'){
            //    $('#dukes_selector').show();
            //}
            //else{
            //    $('#dukes_selector').hide();
            //}
            //
            //if(StagingViewModel.current_icd() === 'C61'){
            //    $('#psa_selector').show();
            //    $('#gleason_selector').show();
            //}
            //else{
            //    $('#psa_selector').hide();
            //    $('#gleason_selector').hide();
            //}

            $.getJSON('get_tnms/' + StagingViewModel.current_icd_neoplasm(), function (json) {
                StagingViewModel.available_ts(json.ts_list);
                StagingViewModel.available_ns(json.ns_list);
                StagingViewModel.available_ms(json.ms_list);
                //StagingViewModel.available_dukes(json.dukes_list);
                //StagingViewModel.available_psa(json.psa_list);
                //StagingViewModel.available_gleason(json.gleason_list);

            });
            },

        tnmChanged:function() {
            if (StagingViewModel.current_t() !== undefined &&
                StagingViewModel.current_n() !== undefined &&
                StagingViewModel.current_m()!== undefined){
                 $.getJSON('get_stage/' + StagingViewModel.current_icd_neoplasm() + '/' + StagingViewModel.current_t() + '/'+
                StagingViewModel.current_n() +'/'+ StagingViewModel.current_m()+ '/'+
                     StagingViewModel.current_dukes() + '/' + StagingViewModel.current_psa(), function (json) {
                    StagingViewModel.calculated_stage(json.stage);
            })
            }


        }
        };

    ko.applyBindings(StagingViewModel);
    StagingViewModel.loadInitialState();
});