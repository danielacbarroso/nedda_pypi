$(function() {
    StagingViewModel = {

        available_icds: ko.observableArray([]),
        available_ts:  ko.observableArray([]),
        available_ns:  ko.observableArray([]),
        available_ms:  ko.observableArray([]),
        current_icd: ko.observable(''),
        current_t:  ko.observable(''),
        current_n:  ko.observable(''),
        current_m:  ko.observable(''),

        loadInitialState: function () {
            $.getJSON('get_icds', function (json) {
                StagingViewModel.available_icds(json.icd_list);
            });
        },

        icdChanged: function () {
            $.getJSON('get_tnms/' + StagingViewModel.current_icd(), function (json) {
                StagingViewModel.available_ts(json.ts_list);
                StagingViewModel.available_ns(json.ns_list);
                StagingViewModel.available_ms(json.ms_list);

            });
            }
        };

    ko.applyBindings(StagingViewModel);
    StagingViewModel.loadInitialState();
});