(function(){
	'use strict';

	angular
		.module('app')
          .controller('configuringController', configuringController);
                        //name                  //function

  function configuringController($scope, $http, configuringFactory){

    $scope.reference = '41';
    $scope.description = 'RF-Module';
    $scope.command = 'RFM41';

 	  $scope.postData = function(){

      var data = {reference: $scope.reference, description: $scope.description, command: $scope.command};
 		  configuringFactory.new_element(data)
           .then(function(response){
 			        $scope.response=response.data;
            }, $scope.response='Duplicated device')  
 	  };

    $scope.upDateData = function(){

      var data = {reference: $scope.reference, description: $scope.description, command: $scope.command};
      configuringFactory.update_element(data)
            .then(function(response){
              $scope.response=response.data;
            })      
    };
  }
})();