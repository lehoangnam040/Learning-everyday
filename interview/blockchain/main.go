package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

type EthError struct {
	Code    int    `json:"code"`
	Message string `json:"message"`
}

func (err EthError) Error() string {
	return fmt.Sprintf("Error %d (%s)", err.Code, err.Message)
}

type Request struct {
	ID      int           `json:"id"`
	JSONRPC string        `json:"jsonrpc"`
	Method  string        `json:"method"`
	Params  []interface{} `json:"params"`
}

type Response struct {
	ID      int             `json:"id"`
	JSONRPC string          `json:"jsonrpc"`
	Result  json.RawMessage `json:"result"`
	Error   *EthError       `json:"error"`
}

type JsonRpcClient struct {
	Url    string
	Client *http.Client
}

func (c *JsonRpcClient) Call(method string, params ...interface{}) (json.RawMessage, error) {
	request := Request{
		ID:      1,
		JSONRPC: "2.0",
		Method:  method,
		Params:  params,
	}

	body, err := json.Marshal(request)
	if err != nil {
		return nil, err
	}
	resp, err := c.Client.Post(c.Url, "application/json", bytes.NewBuffer(body))
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	data, err := io.ReadAll(resp.Body)
	if err != nil {
		return nil, err
	}
	res := new(Response)
	if err := json.Unmarshal(data, res); err != nil {
		return nil, err
	}

	if res.Error != nil {
		return nil, *res.Error
	}

	return res.Result, nil
}

func main() {

	jsonRpcClient := JsonRpcClient{
		Url:    "https://ethereum-rpc.publicnode.com",
		Client: http.DefaultClient,
	}
	var version string
	fmt.Println("Started")
	result, err := jsonRpcClient.Call("eth_blockNumber", "0x407d73d8a49eeb85d32cf465507dd71d507100c1", "latest")
	if err != nil {
		panic(err)
	}
	if err := json.Unmarshal(result, &version); err != nil {
		panic(err)
	}
	fmt.Println(version)
}
