(function(){
	'use strict';

	angular
		.module('app')
          .controller('monitoringController', monitoringController);
              //name                  //function

     function monitoringController($scope, $http){

     	$scope.getData = function(){
     		$http({

     			//withCredentials: true,
     			//headers: {'Content-Type': 'application/json; charset=utf-8'},
     			method: "GET",
     			url: "http://localhost:8000/postmanapp/devices/1"
     		}).then(function(response){
     			$scope.response=response.data;

     		})

          
     	};

     	//$scope.kind = "This is my kind"
     }
})();