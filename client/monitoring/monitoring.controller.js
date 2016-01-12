(function(){
	'use strict';

	angular
		.module('app')
          .controller('monitoringController', monitoringController);
              //name                  //function

     function monitoringController($scope, $http){

          $scope.deviceId = 1;

     	$scope.getData = function(){

               var url = "http://localhost:8000/postmanapp/devices/" + $scope.deviceId + "/";
     		$http({

     			method: "GET",
     			url: url
     		}).then(function(response){
     			$scope.response=response.data;

     		})

          
     	};

          $scope.getAllData = function(){
               $http({

                    method: "GET",
                    url: "http://localhost:8000/postmanapp/devices/"
               }).then(function(response){
                    $scope.response=response.data;

               })
               
          };

     	//$scope.kind = "This is my kind"
     }


})();