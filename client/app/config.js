(function(){
	'use strict';

	angular
		.module('app')
          .config(appConfig);

	function appConfig($stateProvider, $urlRouterProvider) {

    $stateProvider
    .state('monitoring', {
      url: "/monitoring",
      templateUrl: "monitoring/monitoring.html",
      controller: "monitoringController"
    })
    .state('configuring', {
      url: "/configuring",
      templateUrl: "configuring/configuring.html",
      controller: "configuringController"
    });

  	$urlRouterProvider.otherwise("/monitoring");
	}
})();