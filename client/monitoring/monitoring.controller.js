(function(){
	'use strict';

	angular
		.module('app')
          .controller('monitoringController', monitoringController);
              
  function monitoringController($scope, $http, monitoringFactory, $state, $timeout){
  
   	$scope.get_data = function(){
      monitoringFactory.get_element($scope.device_id, $scope.characteristic)
          .then(function(response){
                  $scope.response=response.data.replace( /[^0-9]/g, '' );
                });
   	};

    $scope.get_all_data = function(){
      monitoringFactory.get_all()
          .then(function(response){
                  $scope.response=response.data;
                }) 
    };


    $scope.interval_function = function(){

        $scope.draw_loop = true
        
        $timeout(function() {
        $scope.get_data();
        $scope.interval_function();
        }, 1000)
      

    };





 };
})();

 //http://www.d3noob.org/2014/02/making-bar-chart-in-d3js.html