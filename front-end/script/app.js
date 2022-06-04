const lanIP = `${window.location.hostname}:5000`;
const socket = io(`http://${lanIP}`);

const showTable=function(){

}

const listenToUI = function () {
  let btn = document.querySelector('.js-relais');
  
  let status = 0
  btn.addEventListener('click', (e) => {
  status++
  console.log(status)
  if (status==2){
    status=0
  }
  socket.emit('F2B_sent', {status})
  })};


const listenToSocket = function () {
  socket.on("connected", function () {
    console.log("verbonden met socket webserver");
  });

  socket.on("B2F_send_temp", function (jsonObject) {
    console.log(jsonObject);
    waarde=jsonObject.tempwaarde
    console.log(waarde)
    htmlstring=`temperatuur waarde: ${waarde} ºC`
    document.querySelector('.js-waarde').innerHTML=htmlstring

  });
   
  socket.on("B2F_send_ip", function (jsonObject) {
    // console.log(jsonObject);
    // console.log(jsonObject.slice(2,15))
    ip=jsonObject.slice(2,15)

    document.querySelector('.js-ip').innerHTML= `<p class="js-ip">wifi: ${ip}</p>`

      });
  socket.on("B2F_historiek", function(jsonObject){
    console.log(jsonObject)
    document.querySelector('.js-table').innerHTML+= `
    <tr>
    <td>${jsonObject.volgnummer} </td>
    <td>${jsonObject.deviceid} </td>
    <td>${jsonObject.actieid}</td>
    <td>${jsonObject.actiedatum}</td>
    <td>${jsonObject.waarde}</td>
    <td>${jsonObject.commentaar}</td>
  </tr>`

    
  })
};


document.addEventListener("DOMContentLoaded", function () {
  console.log("DOM geladen 🍺");
  listenToUI();
  listenToSocket();
  showTable();
 
  
});
