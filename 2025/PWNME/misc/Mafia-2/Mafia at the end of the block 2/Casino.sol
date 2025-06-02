// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

contract CasinoPWNME {

  bool public isWinner;
	uint256 public multiplier = 14130161972673258133;
	uint256 public increment = 11367173177704995300;
	uint256 public modulus = 4701930664760306055;
  uint private state; // 3780255856281081491

  constructor (){
    state = block.prevrandao % modulus;
  }

  function checkWin() public view returns (bool) {
    return isWinner;
  }

  // number = 4438878960358861508
  function playCasino(uint number) public payable  {

    require(msg.value >= 0.1 ether, "My brother in christ, it's pay to lose not free to play !");
    PRNG();
    if (number == state){
      isWinner = true;
    } else {
      isWinner = false;
    }
  }
  
  function PRNG() private{
    state = (multiplier * state + increment) % modulus;
  }

}
  

UUID=38b7f9ad-86cd-4924-bdc9-ed09c58f183f
Casino URL=http://mafia2.phreaks.fr:80/38b7f9ad-86cd-4924-bdc9-ed09c58f183f/
RPC=https://mafia2.phreaks.fr/38b7f9ad-86cd-4924-bdc9-ed09c58f183f
PRIVATE_KEY=0x52eedaf87b86200407f800a0901a9066343dd4babc319cd9ec70331a243acb52
PLAYER=0xD769f1a82436e13B53A5dB767423f481440452E9
SETUP=0xcE6E78e6992b14E09429183300f7047939fd0999
TARGET=0xB9523A2DFD1D43878f5b2CEDCa98cCb7214Fa2bA
1000000000000000000