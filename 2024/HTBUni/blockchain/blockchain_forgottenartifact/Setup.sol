// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

import { ForgottenArtifact } from "./ForgottenArtifact.sol";

contract Setup {
    uint256 public constant ARTIFACT_ORIGIN = 0xdead;
    uint256 public deployTimestamp;
    ForgottenArtifact public immutable TARGET;
    
    event DeployedTarget(address at);

    constructor() payable {
        TARGET = new ForgottenArtifact(uint32(ARTIFACT_ORIGIN), address(0));
        deployTimestamp = block.timestamp;
        emit DeployedTarget(address(TARGET));
    }

    function isSolved() public view returns (bool) {
        return TARGET.lastSighting() > deployTimestamp;
    }
}
