(function(){
	'use strict';

	angular
		.module('app')
          .controller('monitoringController', monitoringController);
              
  function monitoringController($scope, $http, monitoringFactory, $state){

    $scope.state = $state
  
   	$scope.getData = function(){
      monitoringFactory.get_element($scope.deviceId)
          .then(function(response){
                  $scope.response=response.data;
                });
   	};

    $scope.getAllData = function(){
      monitoringFactory.get_all()
          .then(function(response){
                  $scope.response=response.data;
                }) 
    };
 };
})();

 //http://www.d3noob.org/2014/02/making-bar-chart-in-d3js.html