import axios from 'axios'
import { paragraphs } from './content'
async function senddata(){
    // paragraphs.forEach(async paragraph => {

        
    // });
    
    const data = await axios.post("http://127.0.0.1:5000/receive_data",{data : "paragraphs[0].innerHTML"})

}

senddata()