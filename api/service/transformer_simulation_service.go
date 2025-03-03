package service

import (
	"context"
	"fmt"

	"github.com/gojek/merlin/config"
	"github.com/gojek/merlin/models"
	"github.com/gojek/merlin/pkg/transformer/executor"
	"github.com/gojek/merlin/pkg/transformer/feast"
	"github.com/gojek/merlin/pkg/transformer/types"

	"go.uber.org/zap"
)

const (
	defaultFeastBatchSize = 50
)

// TransformerService handles the standard transformer simulation
type TransformerService interface {
	// SimulateTransformer simulate transformer execution including preprocessing and postprocessing
	SimulateTransformer(ctx context.Context, simulationPayload *models.TransformerSimulation) (*types.PredictResponse, error)
}

type transformerService struct {
	cfg config.StandardTransformerConfig
}

// NewTransformerService
func NewTransformerService(cfg config.StandardTransformerConfig) TransformerService {
	return &transformerService{
		cfg: cfg,
	}
}

var _ TransformerService = (*transformerService)(nil)

// SimulateTransformer function will call transformer executor that initialize feast serving and do the call to standard transformer
func (ts *transformerService) SimulateTransformer(ctx context.Context, simulationPayload *models.TransformerSimulation) (*types.PredictResponse, error) {
	transformerExecutor, err := ts.createTransformerExecutor(ctx, simulationPayload)
	if err != nil {
		return nil, fmt.Errorf("failed creating transformer executor: %w", err)
	}

	return transformerExecutor.Execute(ctx, simulationPayload.Payload, simulationPayload.Headers), nil
}

func (ts *transformerService) createTransformerExecutor(ctx context.Context, simulationPayload *models.TransformerSimulation) (executor.Transformer, error) {
	var mockModelResponseBody types.JSONObject
	var mockModelRequestHeaders map[string]string

	if simulationPayload.PredictionConfig != nil && simulationPayload.PredictionConfig.Mock != nil {
		if simulationPayload.PredictionConfig.Mock.Body != nil {
			mockModelResponseBody = simulationPayload.PredictionConfig.Mock.Body
		}

		if simulationPayload.PredictionConfig.Mock.Headers != nil {
			mockModelRequestHeaders = simulationPayload.PredictionConfig.Mock.Headers
		}
	}

	// logger := log.GetLogger()
	logger, _ := zap.NewDevelopment()

	transformerExecutor, err := executor.NewStandardTransformerWithConfig(
		ctx,
		simulationPayload.Config,
		executor.WithLogger(logger),
		executor.WithTraceEnabled(true),
		executor.WithModelPredictor(executor.NewMockModelPredictor(mockModelResponseBody, mockModelRequestHeaders, simulationPayload.Protocol)),
		executor.WithFeastOptions(feast.Options{
			StorageConfigs:     ts.cfg.ToFeastStorageConfigsForSimulation(),
			DefaultFeastSource: ts.cfg.DefaultFeastSource,
			BatchSize:          defaultFeastBatchSize,
		}),
		executor.WithProtocol(simulationPayload.Protocol),
	)
	if err != nil {
		return nil, fmt.Errorf("failed initializing standard transformer: %w", err)
	}

	return transformerExecutor, nil
}
