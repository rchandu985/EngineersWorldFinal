import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Student,{JobSeeker,Company} from './Registration_Forms';
import { useState } from 'react';

function HomePageNavBar() {

  const[register_as_student,RegisterAsStudent]=useState(false)
  const[register_as_company,RegisterAsCompany]=useState(false)
  const[register_as_job_seeker,RegisterAsJobSeeker]=useState(false)

    function Enable(value){

        var s = { register_as_student_o: false, register_as_company_o: false,register_as_job_seeker_o:false};

        s[value]=true

        var fact={"register_as_student_o": RegisterAsStudent(s["register_as_student_o"]),"register_as_company_o":RegisterAsCompany(s["register_as_company_o"]),"register_as_job_seeker_o":RegisterAsJobSeeker(s['register_as_job_seeker_o'])}
    }

  return (
    <div>
      <Navbar collapseOnSelect expand="lg" className="bg-body-tertiary" >
          
        <Container>
          <Navbar.Brand href="/">E-World</Navbar.Brand>
          <Navbar.Toggle aria-controls="responsive-navbar-nav" />
          <Navbar.Collapse id="responsive-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link href="#Upload Materials">Upload Materials</Nav.Link>
              <Nav.Link href="#Download Materials">Download Materials</Nav.Link>
              <Nav.Link href="#Login">Login</Nav.Link>
              <NavDropdown title="Register As" id="collapsible-nav-dropdown">
                <NavDropdown.Item onClick={(e) => {e.preventDefault();Enable("register_as_student_o")}} href="#Student">Student</NavDropdown.Item>
                <NavDropdown.Item onClick={(e) => {e.preventDefault();Enable("register_as_company_o")}} href="#Company">Company</NavDropdown.Item>
                <NavDropdown.Item onClick={(e) => {e.preventDefault();Enable("register_as_job_seeker_o")}} href="#Job Seeker">Job Seeker</NavDropdown.Item>
                
              </NavDropdown>
              <Nav.Link href="#Interview Preparations">Interview Preparations</Nav.Link>
              <NavDropdown title="Jobs" id="collapsible-nav-dropdown">
                <NavDropdown.Item href="#State Govt">Student</NavDropdown.Item>
                <NavDropdown.Item href="#Central Govt">Company</NavDropdown.Item>
                <NavDropdown.Item href="#IT Jobs">Job Seeker</NavDropdown.Item>
                
              </NavDropdown>            

            </Nav>

            <Nav>
              
              <Nav.Link href="#Developer">Developer Details</Nav.Link>
              <Nav.Link eventKey={2} href="#Contributions">Contributions</Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
      {register_as_student && <Student/>}
      {register_as_job_seeker && <JobSeeker/>}
      {register_as_company && <Company/>}
    </div>
    
  );
}

export default HomePageNavBar;