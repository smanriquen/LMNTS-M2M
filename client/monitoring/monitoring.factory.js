(function(){
	'use strict';

	angular
		.module('app')
          .factory('monitoringFactory', monitoringFactory);
            
  function monitoringFactory($http){
		return {
      get_all: function() {
  			 return $http({
        				method: "GET",
        				url: "http://localhost:8000/postmanapp/devices/"
     						})
      },
  	
  		get_element: function(element, characteristic){
  			var url = "http://localhost:8000/M2M/machines/" + element + "/characteristics/" + characteristic + "/value";
                                      
  			return $http({
     						method: "GET",
     						url: url
     						})
  		}
 	  };
  }
})();