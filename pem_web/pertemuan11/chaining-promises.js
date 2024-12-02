function proses1() {
    return new Promise((resolve, reject)=> {
        setTimeout(()=>{
            resolve("Hello");
        },1000);
    });
}
function proses2(greetings) {
    return new Promise((resolve, reject)=> {
        setTimeout(()=>{
            resolve(`${greetings} Worlld`);
        },1000);
    });
}
function proses3(pesan) {
    return new Promise((resolve, reject)=> {
        setTimeout(()=>{
            resolve(`${pesan} Have A Great Day`);
        },1000);
    });
}
// memanggil chaining promise
proses1()
.then((greetings)=> {
    return proses2(greetings);
})
.then((pesan)=> {
    return proses3(pesan);
})
.then((result) => {
    console.log(result);
})