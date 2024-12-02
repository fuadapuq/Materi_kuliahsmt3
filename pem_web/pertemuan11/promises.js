function fetchData() {
    return new Promise((resolve, reject)=> {
        setTimeout(() =>{
            const data = "";
            if (data) {
                resolve(data);
            } else {
                reject("Error: Unable to fetch data");
            }
        }, 1000);
    });
}
// Memanggil Promises
fetchData()
.then((data)=>{
    console.log(data);
})
.catch((error)=>{
    console.error(error);
})