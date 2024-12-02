function fetchData(callback){
    setTimeout(function(){
        const data = 'Fetched Data!';
        callback(data);
    },5000);
}
fetchData (function(data){
    console.log(data);
});
// membuat proses 2
console.log ("ini proses2")