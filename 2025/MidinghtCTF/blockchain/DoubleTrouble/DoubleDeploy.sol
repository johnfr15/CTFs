// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

import "./DoubleTrouble.sol";

contract DoubleDeploy {
    event Deployed(address addr);

    bytes32 public constant SALT = keccak256("midnight_ctf");


    function deployFinal() external returns (address) {
        address attack; 
        bytes32 salt = SALT;
        bytes memory attackcode = type(Deployer).creationCode;

        assembly {
            attack := create2(0, add(attackcode, 0x20), mload(attackcode), salt)
        }

        emit Deployed(attack);
        return attack;
    }
}

contract Deployer {
    constructor() {
        if (block.number % 2 == 0) {
            bytes memory b = hex"33ff";
            assembly {
                return(add(b, 0x20), mload(b))
            }
        }
        else {
            bytes memory b = hex"1f1a99ed17babe0000f007b4110000ba5eba110000c0ffee";
            assembly {
                return(add(b, 0x20), mload(b))
            }
        }
    }
}
