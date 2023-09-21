import React from 'react';
import { useState,useEffect } from 'react';
import Select from 'react-select';


import {
  MDBInput,
  MDBCol,
  MDBRow,
  
  MDBBtn,
 
} from 'mdb-react-ui-kit';
import axios from 'axios';


export default function Student() {

    const [formData, setFormData] = useState({username: '',password: '',cell_no:'',email:"",first_name:'',last_name:'',qualification:'',branch:'',year:'',sem:''});
    
    const [qualifications,GetQualifications] =useState()
    const [branches,GetBranches] =useState()
    const [years,GetYears] =useState()
    const [sems,GetSems]=useState()

    const [current_qualification,CurrentQualification]=useState()
    const [current_year,CurrentYear]=useState()
    const [current_branch,CurrentBranch]=useState()
    const [current_sem,CurrentSem]=useState()
    
    const [api_response,Api_Response]=useState('')

    useEffect(()=>{axios.get("fetch_qualifications_data/").then(function(response){GetQualifications(response['data']['qualifications']);})},[])   
      //const [selectedOption, setSelectedOption] = useState(null);
    
      function GetOptionValues(event){
        console.log(event)
        if(event["type"]==="qualification"){

            CurrentQualification(event['value'])
            CurrentBranch([{value:"Select The Branch",label:'Select The Branch'}])
            GetYears()
            CurrentYear([{value:"Select The Branch",label:'Select The Branch'}])
            GetSems()
            CurrentSem([{value:"Select The Year",label:'Select The Year'}])
            console.log(current_year)
            axios.post("fetch_qualifications_data/",{"qualification":event['value'],required_type:"branch"}).then(function(response){GetBranches(response['data']['branches'])})
        }
        else if(event['type']==="branch"){

            CurrentBranch([{value:event['value'],label:event['label']}])
            CurrentYear([{value:"Select The Year",label:'Select The Year'}])
            GetSems()
            CurrentSem([{value:"Select The Year",label:'Select The Year'}])
            axios.post("fetch_qualifications_data/",{"qualification":current_qualification,required_type:"year"}).then(function(response){GetYears(response['data']['years'])})

            //console.log(current_branch)
        }
        else if(event['type']==="year"){
            CurrentYear([{value:event['value'],label:event['value']}])
            GetSems()
            CurrentSem([{value:"Select The Year",label:'Select The Year'}])
            //console.log(current_year[0]['value'])
            axios.post("fetch_qualifications_data/",{"qualification":current_qualification,required_type:"sem"}).then(function(response){GetSems(response['data']['sems'])})

        }
        else if(event["type"]==="sem"){
            CurrentSem([{value:event['value'],label:event['value']}])

        }
      }
      //useEffect(()=>{ },[qualifications])

    
  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData({ ...formData, [name]: value });
  };
  const handleSubmit = (event) => {
    event.preventDefault();

    if (current_branch !== undefined && current_sem !== undefined && current_year !== undefined && current_qualification !==undefined){
    console.log('Submitted Data:', {...formData,year:current_year[0]['value'],sem:current_sem[0]['value'],branch:current_branch[0]['value'],qualification:current_qualification});
    
    

    axios.post('register_as_student/',{...formData,year:current_year[0]['value'],sem:current_sem[0]['value'],branch:current_branch[0]['value'],qualification:current_qualification}).then(function (response) {
      let resp=response['data']
      Api_Response(resp['message'])
      })
    }
    else{
        axios.post('register_as_student/',{...formData,year:'',sem:'',branch:'',qualification:''}).then(function (response) {
      let resp=response['data']
      Api_Response(resp['message'])
      })
    }
}
    

  return (
    <div>
        <br></br>
        <center><h5>{api_response}</h5></center>
        <br></br>
        <form onSubmit={handleSubmit}>
            <div style={{marginLeft:"12cm",marginRight:"12cm"}}>
                <MDBRow className='mb-4'>
                    <MDBCol>
                    <MDBInput id='form3Example1' label='First name' value={formData.first_name} onChange={handleInputChange} name='first_name'/>
                    </MDBCol>
                    <MDBCol>
                    <MDBInput id='form3Example2' label='Last name' name='last_name' value={formData.last_name} onChange={handleInputChange}/>
                    </MDBCol>
                </MDBRow>
                <MDBRow className='mb-4'>
                    <MDBCol>
                    <MDBInput id='form3Example1' label='Username' name='username' value={formData.username} onChange={handleInputChange}/>
                    </MDBCol>
                    <MDBCol>
                    <MDBInput id='form3Example2' label='Password' type='password' name='password' value={formData.password} onChange={handleInputChange}/>
                    </MDBCol>
                </MDBRow>
                <MDBRow className='mb-4'>
                    <MDBCol>
                    <MDBInput id='form3Example1' label='Mobile No' type='text' name='cell_no' value={formData.cell_no} onChange={handleInputChange} />
                    </MDBCol>
                    <MDBCol>
                    <MDBInput id='form3Example2' label='Email Id' type='email' name='email' value={formData.email} onChange={handleInputChange}/>
                    </MDBCol>
                </MDBRow>
                <MDBRow className='mb-4'>
                    <MDBCol>
                        
                        <Select placeholder="Select The Qualification"   onChange={GetOptionValues} options={qualifications}/>
                    </MDBCol>
                    <MDBCol>
                        <Select placeholder="Select The Branch" value={current_branch}  onChange={GetOptionValues}  options={branches}/>
                    </MDBCol>
                </MDBRow>

                <MDBRow className='mb-4'>
                    <MDBCol>
                        
                        <Select placeholder="Select The Year" value={current_year}   onChange={GetOptionValues} options={years}/>
                    </MDBCol>
                    <MDBCol>
                        <Select placeholder="Select The Sem" value={current_sem}   onChange={GetOptionValues} options={sems}/>

                    </MDBCol>
                </MDBRow>



                <MDBBtn type='submit' className='mb-4' block>
                    Register
                </MDBBtn>
            </div>
        
        </form>
    </div>
  );
}

export  function JobSeeker() {

    const [formData, setFormData] = useState({username: '',password: '',cell_no:'',email:"",first_name:'',last_name:'',qualification:'',branch:''});
    
    const [qualifications,GetQualifications] =useState()
    const [branches,GetBranches] =useState()


    const [current_qualification,CurrentQualification]=useState()
    
    const [current_branch,CurrentBranch]=useState()
    
    
    const [api_response,Api_Response]=useState('')

    useEffect(()=>{axios.get("fetch_qualifications_data/").then(function(response){GetQualifications(response['data']['qualifications']);})},[])   
      //const [selectedOption, setSelectedOption] = useState(null);
    
      function GetOptionValues(event){
        console.log(event)
        if(event["type"]==="qualification"){

            CurrentQualification(event['value'])
            CurrentBranch([{value:"Select The Branch",label:'Select The Branch'}])
            
            axios.post("fetch_qualifications_data/",{"qualification":event['value'],required_type:"branch"}).then(function(response){GetBranches(response['data']['branches'])})
        }
        else if(event['type']==="branch"){

            CurrentBranch([{value:event['value'],label:event['label']}])
        }
    }
    
  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData({ ...formData, [name]: value });
  };
  const handleSubmit = (event) => {
    event.preventDefault();

    //console.log(current_year,current_branch[0]['value'])
    // Access the form data from the state
    //const { username, password ,email} = formData;

    // Do something with the form data, e.g., send it to an API, perform validation, etc.
    if (current_branch !== undefined &&  current_qualification !==undefined){

    console.log('Submitted Data:', {...formData,branch:current_branch[0]['value'],qualification:current_qualification});
    
    

    axios.post('register_as_job_searcher/',{...formData,branch:current_branch[0]['value'],qualification:current_qualification}).then(function (response) {
      let resp=response['data']
      Api_Response(resp['message'])
      })
    }
    else{

        axios.post('register_as_job_searcher/',{...formData,branch:'',qualification:''}).then(function (response) {
      let resp=response['data']
      Api_Response(resp['message'])
      })

    }

    }

  return (
    <div>
        <br></br>
        <center><h5>{api_response}</h5></center>
        <br></br>
        <form onSubmit={handleSubmit}>
            <div style={{marginLeft:"12cm",marginRight:"12cm"}}>
                <MDBRow className='mb-4'>
                    <MDBCol>
                    <MDBInput id='form3Example1' label='First name' value={formData.first_name} onChange={handleInputChange} name='first_name'/>
                    </MDBCol>
                    <MDBCol>
                    <MDBInput id='form3Example2' label='Last name' name='last_name' value={formData.last_name} onChange={handleInputChange}/>
                    </MDBCol>
                </MDBRow>
                <MDBRow className='mb-4'>
                    <MDBCol>
                    <MDBInput id='form3Example1' label='Username' name='username' value={formData.username} onChange={handleInputChange}/>
                    </MDBCol>
                    <MDBCol>
                    <MDBInput id='form3Example2' label='Password' type='password' name='password' value={formData.password} onChange={handleInputChange}/>
                    </MDBCol>
                </MDBRow>
                <MDBRow className='mb-4'>
                    <MDBCol>
                    <MDBInput id='form3Example1' label='Mobile No' type='text' name='cell_no' value={formData.cell_no} onChange={handleInputChange} />
                    </MDBCol>
                    <MDBCol>
                    <MDBInput id='form3Example2' label='Email Id' type='email' name='email' value={formData.email} onChange={handleInputChange}/>
                    </MDBCol>
                </MDBRow>
                <MDBRow className='mb-4'>
                    <MDBCol>
                        
                        <Select placeholder="Select The Qualification"   onChange={GetOptionValues} options={qualifications}/>
                    </MDBCol>
                    <MDBCol>
                        <Select placeholder="Select The Branch" value={current_branch}  onChange={GetOptionValues}  options={branches}/>
                    </MDBCol>
                </MDBRow>

                


                <MDBBtn type='submit' className='mb-4' block>
                    Register
                </MDBBtn>
            </div>
        
        </form>
    </div>
  );
}

export  function Company() {

    const [formData, setFormData] = useState({username: '',password: '',cell_no:'',email:"",first_name:'',last_name:'',company_name:'',designation:''});
    const [api_response,Api_Response]=useState('')

    
  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData({ ...formData, [name]: value });
  };
  const handleSubmit = (event) => {
    event.preventDefault();

    //console.log(current_year,current_branch[0]['value'])
    // Access the form data from the state
    //const { username, password ,email} = formData;

    // Do something with the form data, e.g., send it to an API, perform validation, etc.
    
        axios.post('register_as_company/',{...formData}).then(function (response) {
      let resp=response['data']
      Api_Response(resp['message'])
      })

    

    }

  return (
    <div>
        <br></br>
        <center><h5>{api_response}</h5></center>
        <br></br>
        <form onSubmit={handleSubmit}>
            <div style={{marginLeft:"12cm",marginRight:"12cm"}}>
                <MDBRow className='mb-4'>
                    <MDBCol>
                    <MDBInput id='form3Example1' label='First name' value={formData.first_name} onChange={handleInputChange} name='first_name'/>
                    </MDBCol>
                    <MDBCol>
                    <MDBInput id='form3Example2' label='Last name' name='last_name' value={formData.last_name} onChange={handleInputChange}/>
                    </MDBCol>
                </MDBRow>
                <MDBRow className='mb-4'>
                    <MDBCol>
                    <MDBInput id='form3Example1' label='Username' name='username' value={formData.username} onChange={handleInputChange}/>
                    </MDBCol>
                    <MDBCol>
                    <MDBInput id='form3Example2' label='Password' type='password' name='password' value={formData.password} onChange={handleInputChange}/>
                    </MDBCol>
                </MDBRow>
                <MDBRow className='mb-4'>
                    <MDBCol>
                    <MDBInput id='form3Example1' label='Mobile No' type='text' name='cell_no' value={formData.cell_no} onChange={handleInputChange} />
                    </MDBCol>
                    <MDBCol>
                    <MDBInput id='form3Example2' label='Email Id' type='email' name='email' value={formData.email} onChange={handleInputChange}/>
                    </MDBCol>
                </MDBRow>
                
                <MDBRow className='mb-4'>
                    <MDBCol>
                    <MDBInput id='form3Example1' label='Company Name' type='text' name='company_name' value={formData.company_name} onChange={handleInputChange} />
                    </MDBCol>
                    <MDBCol>
                    <MDBInput id='form3Example2' label='Designation' type='email' name='designation' value={formData.designation} onChange={handleInputChange}/>
                    </MDBCol>
                </MDBRow>
                


                <MDBBtn type='submit' className='mb-4' block>
                    Register
                </MDBBtn>
            </div>
        
        </form>
    </div>
  );
}

