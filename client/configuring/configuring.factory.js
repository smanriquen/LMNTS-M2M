(function(){
	'use strict';

	angular
		.module('app')
          .factory('configuringFactory', configuringFactory);
              //name                  //function

  function configuringFactory($http){
		return {
      new_element: function(data) {
        return $http.post("http://localhost:8000/postmanapp/devices/", data, {
            		headers : {'Content-Type' : 'application/json; charset=UTF-8'}
      					})
      },
    	
    	update_element: function(data){
    		var url = "http://localhost:8000/postmanapp/devices/" + data.reference + "/";
    		return $http.put(url, data, {
            			headers : {'Content-Type' : 'application/json; charset=UTF-8'}
      					})
    	}
   	};
	}	
})();