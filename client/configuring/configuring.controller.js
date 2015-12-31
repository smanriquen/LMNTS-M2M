(function(){
	'use strict';

	angular
		.module('app')
          .controller('configuringController', configuringController);
              //name                  //function

     function configuringController($scope, $http){

     	$scope.postData = function(){
     		$http.post("http://localhost:8000/postmanapp/devices/", {"kind": "RF-Module", "model": "RFM1","comment":"RFM1 Talking!"}, {
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