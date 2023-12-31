# coding: utf-8

"""
    HTTP API Console

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.service_api import ServiceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestServiceApi(unittest.TestCase):
    """ServiceApi unit test stubs"""

    def setUp(self):
        self.api = ServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cosmos_base_node_v1_beta1_config(self):
        """Test case for cosmos_base_node_v1_beta1_config

        Config queries for the operator configuration.  # noqa: E501
        """
        pass

    def test_cosmos_base_tendermint_v1_beta1_abci_query(self):
        """Test case for cosmos_base_tendermint_v1_beta1_abci_query

        ABCIQuery defines a query handler that supports ABCI queries directly to the application, bypassing Tendermint completely. The ABCI query must contain a valid and supported path, including app, custom, p2p, and store.  # noqa: E501
        """
        pass

    def test_cosmos_base_tendermint_v1_beta1_get_block_by_height(self):
        """Test case for cosmos_base_tendermint_v1_beta1_get_block_by_height

        GetBlockByHeight queries block for given height.  # noqa: E501
        """
        pass

    def test_cosmos_base_tendermint_v1_beta1_get_latest_block(self):
        """Test case for cosmos_base_tendermint_v1_beta1_get_latest_block

        GetLatestBlock returns the latest block.  # noqa: E501
        """
        pass

    def test_cosmos_base_tendermint_v1_beta1_get_latest_validator_set(self):
        """Test case for cosmos_base_tendermint_v1_beta1_get_latest_validator_set

        GetLatestValidatorSet queries latest validator-set.  # noqa: E501
        """
        pass

    def test_cosmos_base_tendermint_v1_beta1_get_node_info(self):
        """Test case for cosmos_base_tendermint_v1_beta1_get_node_info

        GetNodeInfo queries the current node info.  # noqa: E501
        """
        pass

    def test_cosmos_base_tendermint_v1_beta1_get_syncing(self):
        """Test case for cosmos_base_tendermint_v1_beta1_get_syncing

        GetSyncing queries node syncing.  # noqa: E501
        """
        pass

    def test_cosmos_base_tendermint_v1_beta1_get_validator_set_by_height(self):
        """Test case for cosmos_base_tendermint_v1_beta1_get_validator_set_by_height

        GetValidatorSetByHeight queries validator-set at a given height.  # noqa: E501
        """
        pass

    def test_cosmos_tx_v1_beta1_broadcast_tx(self):
        """Test case for cosmos_tx_v1_beta1_broadcast_tx

        BroadcastTx broadcast transaction.  # noqa: E501
        """
        pass

    def test_cosmos_tx_v1_beta1_get_block_with_txs(self):
        """Test case for cosmos_tx_v1_beta1_get_block_with_txs

        GetBlockWithTxs fetches a block with decoded txs.  # noqa: E501
        """
        pass

    def test_cosmos_tx_v1_beta1_get_tx(self):
        """Test case for cosmos_tx_v1_beta1_get_tx

        GetTx fetches a tx by hash.  # noqa: E501
        """
        pass

    def test_cosmos_tx_v1_beta1_get_txs_event(self):
        """Test case for cosmos_tx_v1_beta1_get_txs_event

        GetTxsEvent fetches txs by event.  # noqa: E501
        """
        pass

    def test_cosmos_tx_v1_beta1_simulate(self):
        """Test case for cosmos_tx_v1_beta1_simulate

        Simulate simulates executing a transaction for estimating gas usage.  # noqa: E501
        """
        pass

    def test_cosmos_tx_v1_beta1_tx_decode(self):
        """Test case for cosmos_tx_v1_beta1_tx_decode

        TxDecode decodes the transaction.  # noqa: E501
        """
        pass

    def test_cosmos_tx_v1_beta1_tx_decode_amino(self):
        """Test case for cosmos_tx_v1_beta1_tx_decode_amino

        TxDecodeAmino decodes an Amino transaction from encoded bytes to JSON.  # noqa: E501
        """
        pass

    def test_cosmos_tx_v1_beta1_tx_encode(self):
        """Test case for cosmos_tx_v1_beta1_tx_encode

        TxEncode encodes the transaction.  # noqa: E501
        """
        pass

    def test_cosmos_tx_v1_beta1_tx_encode_amino(self):
        """Test case for cosmos_tx_v1_beta1_tx_encode_amino

        TxEncodeAmino encodes an Amino transaction from JSON to encoded bytes.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
