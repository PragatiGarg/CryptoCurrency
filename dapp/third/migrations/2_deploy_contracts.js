var Vote = artifacts.require("./Vote.sol");
module.exports = function(deployer) {
  // deployer.deploy(Voting, 1000, web3.toWei('0.1', 'ether'), ['CandidateA', 'CandidateB', 'CandidateC']);
  deployer.deploy(Vote, 1000, web3.toWei('0.1', 'ether'), ['CandidateA', 'CandidateB', 'CandidateC'], {
    gas: 6700000
  });

};
