pragma solidity >=0.4.22 <0.6.0;

import "./Owner.sol";

contract BlockSale is Owner{

    /* Buyer and Seller is called Customer*/
    struct Customer{
        uint[] products;
    }

    mapping(address => Customer) customers;
    event SaleComplete(address from, address to);

    function buy(address buyer,address seller, uint amount, uint productid) public{
        //subtract money
        if (balances[buyer] < amount) return;
        balances[buyer] -= amount;
        balances[seller] += amount;
        emit SaleComplete(buyer, seller);

        //pop productid
        for (uint i = 0; i < customers[seller].products.length - 1; i++) {
          if(customers[seller].products[i] == productid){
              delete customers[seller].products[i];
              for (uint k = i; k < customers[seller].products.length - 1; k++){
                  customers[seller].products[k] = customers[seller].products[k+1];
              }
              delete customers[seller].products[customers[seller].products.length - 1];
              customers[seller].products.length--;
              break;
          }
        }

        //push product
        customers[buyer].products.push(productid);
    }

    function addproduct(address own, uint productid) public{
        customers[own].products.push(productid);
    }

    function removeProduct(address own, uint productid) public{
        //remove product
        for (uint i = 0; i < customers[own].products.length - 1; i++) {
          if(customers[own].products[i] == productid){
              delete customers[own].products[i];
              for (uint k = i; k < customers[own].products.length - 1; k++){
                  customers[own].products[k] = customers[own].products[k+1];
              }
              delete customers[own].products[customers[own].products.length - 1];
              customers[own].products.length--;
              break;
          }
        }
    }

    function showProduct(address cust) public returns (uint[] memory){
        return customers[cust].products;
    }
}
