// Code generated by MockGen. DO NOT EDIT.
// Source: github.com/Azure/ARO-RP/pkg/util/azureclient/mgmt/containerregistry (interfaces: TokensClient,RegistriesClient)

// Package mock_containerregistry is a generated GoMock package.
package mock_containerregistry

import (
	context "context"
	reflect "reflect"

	containerregistry "github.com/Azure/azure-sdk-for-go/services/containerregistry/mgmt/2019-06-01-preview/containerregistry"
	gomock "github.com/golang/mock/gomock"
)

// MockTokensClient is a mock of TokensClient interface
type MockTokensClient struct {
	ctrl     *gomock.Controller
	recorder *MockTokensClientMockRecorder
}

// MockTokensClientMockRecorder is the mock recorder for MockTokensClient
type MockTokensClientMockRecorder struct {
	mock *MockTokensClient
}

// NewMockTokensClient creates a new mock instance
func NewMockTokensClient(ctrl *gomock.Controller) *MockTokensClient {
	mock := &MockTokensClient{ctrl: ctrl}
	mock.recorder = &MockTokensClientMockRecorder{mock}
	return mock
}

// EXPECT returns an object that allows the caller to indicate expected use
func (m *MockTokensClient) EXPECT() *MockTokensClientMockRecorder {
	return m.recorder
}

// CreateAndWait mocks base method
func (m *MockTokensClient) CreateAndWait(arg0 context.Context, arg1, arg2, arg3 string, arg4 containerregistry.Token) error {
	m.ctrl.T.Helper()
	ret := m.ctrl.Call(m, "CreateAndWait", arg0, arg1, arg2, arg3, arg4)
	ret0, _ := ret[0].(error)
	return ret0
}

// CreateAndWait indicates an expected call of CreateAndWait
func (mr *MockTokensClientMockRecorder) CreateAndWait(arg0, arg1, arg2, arg3, arg4 interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "CreateAndWait", reflect.TypeOf((*MockTokensClient)(nil).CreateAndWait), arg0, arg1, arg2, arg3, arg4)
}

// DeleteAndWait mocks base method
func (m *MockTokensClient) DeleteAndWait(arg0 context.Context, arg1, arg2, arg3 string) error {
	m.ctrl.T.Helper()
	ret := m.ctrl.Call(m, "DeleteAndWait", arg0, arg1, arg2, arg3)
	ret0, _ := ret[0].(error)
	return ret0
}

// DeleteAndWait indicates an expected call of DeleteAndWait
func (mr *MockTokensClientMockRecorder) DeleteAndWait(arg0, arg1, arg2, arg3 interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "DeleteAndWait", reflect.TypeOf((*MockTokensClient)(nil).DeleteAndWait), arg0, arg1, arg2, arg3)
}

// MockRegistriesClient is a mock of RegistriesClient interface
type MockRegistriesClient struct {
	ctrl     *gomock.Controller
	recorder *MockRegistriesClientMockRecorder
}

// MockRegistriesClientMockRecorder is the mock recorder for MockRegistriesClient
type MockRegistriesClientMockRecorder struct {
	mock *MockRegistriesClient
}

// NewMockRegistriesClient creates a new mock instance
func NewMockRegistriesClient(ctrl *gomock.Controller) *MockRegistriesClient {
	mock := &MockRegistriesClient{ctrl: ctrl}
	mock.recorder = &MockRegistriesClientMockRecorder{mock}
	return mock
}

// EXPECT returns an object that allows the caller to indicate expected use
func (m *MockRegistriesClient) EXPECT() *MockRegistriesClientMockRecorder {
	return m.recorder
}

// GenerateCredentials mocks base method
func (m *MockRegistriesClient) GenerateCredentials(arg0 context.Context, arg1, arg2 string, arg3 containerregistry.GenerateCredentialsParameters) (containerregistry.GenerateCredentialsResult, error) {
	m.ctrl.T.Helper()
	ret := m.ctrl.Call(m, "GenerateCredentials", arg0, arg1, arg2, arg3)
	ret0, _ := ret[0].(containerregistry.GenerateCredentialsResult)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

// GenerateCredentials indicates an expected call of GenerateCredentials
func (mr *MockRegistriesClientMockRecorder) GenerateCredentials(arg0, arg1, arg2, arg3 interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "GenerateCredentials", reflect.TypeOf((*MockRegistriesClient)(nil).GenerateCredentials), arg0, arg1, arg2, arg3)
}
