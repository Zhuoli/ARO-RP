// Code generated by MockGen. DO NOT EDIT.
// Source: github.com/Azure/ARO-RP/pkg/util/encryption (interfaces: Cipher)

// Package mock_encryption is a generated GoMock package.
package mock_encryption

import (
	reflect "reflect"

	gomock "github.com/golang/mock/gomock"
)

// MockCipher is a mock of Cipher interface
type MockCipher struct {
	ctrl     *gomock.Controller
	recorder *MockCipherMockRecorder
}

// MockCipherMockRecorder is the mock recorder for MockCipher
type MockCipherMockRecorder struct {
	mock *MockCipher
}

// NewMockCipher creates a new mock instance
func NewMockCipher(ctrl *gomock.Controller) *MockCipher {
	mock := &MockCipher{ctrl: ctrl}
	mock.recorder = &MockCipherMockRecorder{mock}
	return mock
}

// EXPECT returns an object that allows the caller to indicate expected use
func (m *MockCipher) EXPECT() *MockCipherMockRecorder {
	return m.recorder
}

// Decrypt mocks base method
func (m *MockCipher) Decrypt(arg0 []byte) ([]byte, error) {
	m.ctrl.T.Helper()
	ret := m.ctrl.Call(m, "Decrypt", arg0)
	ret0, _ := ret[0].([]byte)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

// Decrypt indicates an expected call of Decrypt
func (mr *MockCipherMockRecorder) Decrypt(arg0 interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "Decrypt", reflect.TypeOf((*MockCipher)(nil).Decrypt), arg0)
}

// Encrypt mocks base method
func (m *MockCipher) Encrypt(arg0 []byte) ([]byte, error) {
	m.ctrl.T.Helper()
	ret := m.ctrl.Call(m, "Encrypt", arg0)
	ret0, _ := ret[0].([]byte)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

// Encrypt indicates an expected call of Encrypt
func (mr *MockCipherMockRecorder) Encrypt(arg0 interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "Encrypt", reflect.TypeOf((*MockCipher)(nil).Encrypt), arg0)
}
