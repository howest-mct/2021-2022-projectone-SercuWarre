const lanIP = `${window.location.hostname}:5000`;
const socket = io(`http://${lanIP}`);

const showTable=function(){
    socket.on("B2F_historiek", function(jsonObject){
    // console.log(jsonObject)
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

}
const grafiek=function(){
  socket.on("B2F_temp_chart",function(jsonObject){
    let labels = [
    
  ];
  let datas=[

  ]
  // console.log(jsonObject)
 for (const item of jsonObject.waarde){
  //  console.log(item)
      labels.push(item.actiedatum)
      datas.push(item.waarde)
 }
  
  // console.log(datelist)
 

  const data = {
    labels: labels,
    datasets: [{
      label: 'My First dataset',
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgb(255, 99, 132)',
      data: datas,
    }]
  };

  const config = {
    type: 'line',
    data: data,
    options: {}
  };
  const myChart = new Chart(
    document.getElementById('myChart'),
    config
  );
  myChart()
}
)}



const listenToUI = function () {
 if(window.location.pathname=='/index.html'){
  let btn = document.querySelector('.js-relais');
  console.log(btn)
  let status = 0
  btn.addEventListener('click', (e) => {
  status++
  console.log(status)
  if (status==2){
    status=0
  }
  socket.emit('F2B_sent', {status})
  })};
}

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

};


document.addEventListener("DOMContentLoaded", function () {
  console.log("DOM geladen 🍺");
  if(window.location.pathname=='/'){
  listenToUI();
  listenToSocket();
  } 
  if(window.location.pathname=='/historiek.html'){
  showTable();
  grafiek()
  }
  
});
