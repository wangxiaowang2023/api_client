# CosmosTxV1beta1ModeInfoSingle

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | SignMode represents a signing mode with its own security guarantees.  This enum should be considered a registry of all known sign modes in the Cosmos ecosystem. Apps are not expected to support all known sign modes. Apps that would like to support custom  sign modes are encouraged to open a small PR against this file to add a new case to this SignMode enum describing their sign mode so that different apps have a consistent version of this enum.   - SIGN_MODE_UNSPECIFIED: SIGN_MODE_UNSPECIFIED specifies an unknown signing mode and will be rejected.  - SIGN_MODE_DIRECT: SIGN_MODE_DIRECT specifies a signing mode which uses SignDoc and is verified with raw bytes from Tx.  - SIGN_MODE_TEXTUAL: SIGN_MODE_TEXTUAL is a future signing mode that will verify some human-readable textual representation on top of the binary representation from SIGN_MODE_DIRECT. It is currently not supported.  - SIGN_MODE_DIRECT_AUX: SIGN_MODE_DIRECT_AUX specifies a signing mode which uses SignDocDirectAux. As opposed to SIGN_MODE_DIRECT, this sign mode does not require signers signing over other signers&#x27; &#x60;signer_info&#x60;. It also allows for adding Tips in transactions.  Since: cosmos-sdk 0.46  - SIGN_MODE_LEGACY_AMINO_JSON: SIGN_MODE_LEGACY_AMINO_JSON is a backwards compatibility mode which uses Amino JSON and will be removed in the future.  - SIGN_MODE_EIP_191: SIGN_MODE_EIP_191 specifies the sign mode for EIP 191 signing on the Cosmos SDK. Ref: https://eips.ethereum.org/EIPS/eip-191  Currently, SIGN_MODE_EIP_191 is registered as a SignMode enum variant, but is not implemented on the SDK by default. To enable EIP-191, you need to pass a custom &#x60;TxConfig&#x60; that has an implementation of &#x60;SignModeHandler&#x60; for EIP-191. The SDK may decide to fully support EIP-191 in the future.  Since: cosmos-sdk 0.45.2 | [optional] [default to 'SIGN_MODE_UNSPECIFIED']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
