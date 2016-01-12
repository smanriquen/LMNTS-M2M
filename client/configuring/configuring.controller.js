(function(){
	'use strict';

	angular
		.module('app')
          .controller('configuringController', configuringController);
              //name                  //function

     function configuringController($scope, $http){

        $scope.reference = '41';
        $scope.description = 'RF-Module';
        $scope.command = 'RFM41';

     	$scope.postData = function(){


        var data = {reference: $scope.reference, description: $scope.description, command: $scope.command};
     		$http.post("http://localhost:8000/postmanapp/devices/", data, {
              headers : {
                'Content-Type' : 'application/json; charset=UTF-8'
            }

        }).then(function(response){
     			$scope.response=response.data;

     		}, $scope.response='Duplicated device')

          
          
     	};


      $scope.upDateData = function(){


        var data = {reference: $scope.reference, description: $scope.description, command: $scope.command};
        var url = "http://localhost:8000/postmanapp/devices/" + $scope.reference + "/";
        $http.put(url, data, {
              headers : {
                'Content-Type' : 'application/json; charset=UTF-8'
            }

        }).then(function(response){
          $scope.response=response.data;

        })

          
      };

     	//$scope.kind = "This is my kind"
     }
})();