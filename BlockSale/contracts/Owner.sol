pragma solidity >=0.4.22 <0.6.0;
contract Owner{
    address minter;
    mapping (address => uint) public balances;

    event Create(address from, address to);
    event Delete(address from, address to);
    event Sent(address from, address to, uint amount);

    constructor() public{
        minter = msg.sender;
    }

    // modifier to check the function is executed by Contract Deployer Only
    modifier onlyOwner()
     {  require(msg.sender == minter);
       _;
     }

    // Only Owner can mint money
    function mint( uint amount) public onlyOwner {
        balances[msg.sender] += amount;
    }

    // Only Owner can create user with default balance 500, given Owner has balance
    function createUser(address receiver) public onlyOwner{
        if (balances[msg.sender] < 500) {revert();}
        balances[msg.sender] -= 500;
        balances[receiver] = 500;
        emit Create(msg.sender, receiver);
    }

    // Only Owner can delete user and balance is transfered to Owner
    function deleteUser(address receiver) public onlyOwner{
        balances[msg.sender] += balances[receiver];
        balances[receiver] = 0;
        emit Delete(msg.sender, receiver);
    }

    // Only Owner can add balance, given Owner has sufficent balance
    function addMoneyUser(address receiver, uint amount) public onlyOwner{
        if (balances[msg.sender] < amount) {revert();}
        balances[msg.sender] -= amount;
        balances[receiver] += amount;
        emit Sent(msg.sender, receiver, amount);
    }
}
