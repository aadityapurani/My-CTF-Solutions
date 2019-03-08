Java.perform(function(){
	
	// Step - 1 
	
	var array_list = Java.use("java.util.ArrayList");
    var ApiClient = Java.use('com.android.org.conscrypt.TrustManagerImpl');

    ApiClient.checkTrustedRecursive.implementation = function(a1, a2, a3, a4, a5, a6) {
        var k = array_list.$new();
        return k;
    }
	
	
	// Step - 2
	
	console.log("Hookin Java");
		
    const StringBuilder = Java.use('java.lang.StringBuilder');
		
	StringBuilder.$init.overload('java.lang.String').implementation = function (arg) {
            var partial = "";
            var result = this.$init(arg);
            console.log('new StringBuilder("' + result + '");')
            return result;
    }
    
	console.log("Hooking new StringBuilder(java.lang.String)");
  
  
    // Step - 3

    StringBuilder.toString.implementation = function () {
            var result = this.toString();
            console.log('StringBuilder.toString(); => ' + result)
            return result;
    }
    
	console.log("Hooking StringBuilder.toString() hooked");
	
}, 0);
