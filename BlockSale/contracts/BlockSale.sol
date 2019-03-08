pragma solidity >=0.4.22 <0.6.0;

import "./Owner.sol";

contract BlockSale is Owner{

    bytes32 public transactionHash;
    event SaleComplete(address from, address to);

    function buy(bytes memory productString) public{
         transactionHash = keccak256(productString);
    }

    
    function settlePayment(address buyer,address seller, uint amount) public{
        //subtract money
        if (balances[buyer] < amount) return;
        balances[buyer] -= amount;
        balances[seller] += amount;
        emit SaleComplete(buyer, seller);
        
    }
}
