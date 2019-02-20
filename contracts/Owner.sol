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

    function mint( uint amount) public  {
        if (msg.sender != minter) return;
        balances[msg.sender] += amount;
    }

    function createUser(address receiver) public {
        if (balances[msg.sender] < 500) return;
        balances[msg.sender] -= 500;
        balances[receiver] = 500;
        emit Create(msg.sender, receiver);
    }

    function deleteUser(address receiver) public {
        balances[msg.sender] += balances[receiver];
        balances[receiver] = 0;
        emit Delete(msg.sender, receiver);
    }

    function addMoneyUser(address receiver, uint amount) public{
        if (balances[msg.sender] < amount) return;
        balances[msg.sender] -= amount;
        balances[receiver] += amount;
        emit Sent(msg.sender, receiver, amount);

    }
}
