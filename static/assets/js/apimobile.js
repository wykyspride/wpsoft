function apimobile(){
    fetch ('Test_SmartPayGateWay_Melogerici.postman_collection.json')
    .then(res=>res.json)
    .then(data=console.log(JSON.stringify(data)))
}
