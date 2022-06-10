const lanIP = `${window.location.hostname}:5000`;
const socket = io(`http://${lanIP}`);

const showTable=function(){
  socket.on("B2F_historiek", function(jsonObject){
      htmlLijst=[]
    // console.log(jsonObject)
    for(const item of jsonObject){
     lijst= `
      <tr>
      <td>${item.volgnummer} </td>
      <td>${item.deviceid} </td>
      <td>${item.actieid}</td>
      <td>${item.actiedatum}</td>
      <td>${item.waarde}</td>
      <td>${item.commentaar}</td>
    </tr>`
    htmlLijst+=lijst
    }
    document.querySelector('.js-table').innerHTML=htmlLijst

    
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
      label: 'Temperatuur',
      backgroundColor: 'rgb(255, 0, 0)',
      borderColor: 'rgb(255, 0, 0)',
      data: datas,
    }]
  };

  const config = {
    type: 'line',
    data: data,
    options: {
     scales: {
      y: {
        min: 15,
        max: 30,
      }
      
    }
    }
  };
  const myChart = new Chart(
    document.getElementById('myChart'),
    config
  );
  myChart()
}
)}



const listenToUI = function () {

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

  }  
  )

};

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
const frigo=function(){
    socket.on("B2F_Frigo",function(){
    console.log('hi')
    window.location.replace("192.168.168.169/frigo");
    window.location.pathname='/frigo.html'
   
  });
   const log=document.querySelectorAll('.js-plus')
   
   for (let item of log){
  
     item .addEventListener("click",function(){
       const input =item.parentNode.querySelector('input')  
       input.value++
      //  console.log(input.value)
      })

   }
    const btn=document.querySelectorAll('.js-minus')
   
   for (let item of btn){

     item.addEventListener("click",function(){
       const input =item.parentNode.querySelector('input')  
       if (input.value>0){
         input.value--

       }
      //  console.log(input.value)
      })

   }
   const submit=document.querySelector('.js-submit')
   submit.addEventListener("click",function(){
     let quantity=document.querySelectorAll('.js-quantity')
     for(let btn of quantity){
       console.log(btn.value)
       window.location.replace("/")

     }
    //  console.log(quantity)
   })

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
  frigo()
});
