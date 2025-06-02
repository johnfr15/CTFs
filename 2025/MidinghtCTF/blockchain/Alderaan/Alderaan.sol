// Author : Neoreo
// Difficulty : Easy

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

contract Alderaan {
    event AlderaanDestroyed(address indexed destroyer, uint256 amount);
    bool public isSolved = false;

    constructor() payable{
        require(msg.value > 0,"Contract require some ETH !");
    }

    function DestroyAlderaan(string memory _key) public payable {
        require(msg.value > 0, "Hey, send me some ETH !");
        require(
            keccak256(abi.encodePacked(_key)) == keccak256(abi.encodePacked("ObiWanCantSaveAlderaan")),
            "Incorrect key"
        );

        emit AlderaanDestroyed(msg.sender, address(this).balance);

        isSolved = true;
        selfdestruct(payable(msg.sender));
    }
}


// API: ctfd_120d3253e82fee7cf392c04d9e9415f7cf207792173af1124d2bdf99044b72a2