import React from "react";
import { EuiButtonIcon, EuiFieldText, EuiSuperSelect } from "@elastic/eui";
import { get, InMemoryTableForm, useOnChangeHandler } from "@gojek/mlp-ui";
import { JsonPathConfigInput } from "../../JsonPathConfigInput";
import "../../RowCell.scss";

export const VariablesInput = ({ variables, onChangeHandler, errors = {} }) => {
  const { onChange } = useOnChangeHandler(onChangeHandler);

  const items = [
    ...variables.map((v, idx) => ({ idx, ...v })),
    { idx: variables.length }
  ];

  const onDeleteVariable = idx => () => {
    variables.splice(idx, 1);
    onChangeHandler(variables);
  };

  const typeOptions = [
    { value: "jsonpath", inputDisplay: "JSONPath" },
    { value: "expression", inputDisplay: "Expression" },
    { value: "string", inputDisplay: "String literal" },
    { value: "int", inputDisplay: "Integer literal" },
    { value: "float", inputDisplay: "Float literal" },
    { value: "bool", inputDisplay: "Boolean literal" }
  ];

  const onVariableChange = (idx, field, value) => {
    let newItem = { ...items[idx], [field]: value };
    if ("literal" in newItem) {
      delete newItem["literal"];
    }
    if ("expression" in newItem) {
      delete newItem["expression"];
    }
    if ("jsonPathConfig" in newItem) {
      delete newItem["jsonPathConfig"];
    }
    if (newItem.name === undefined) {
      newItem.name = "";
    }
    if ("idx" in newItem) {
      delete newItem.idx;
    }

    //flatten value type for non-jsonpath type
    if (newItem.type !== "jsonpath" && typeof newItem.value === "object") {
      newItem["value"] = newItem.value.jsonPath;
    }

    switch (newItem.type) {
      case "jsonpath":
        if (newItem.value && newItem.value.jsonPath === undefined) {
          newItem["value"] = { jsonPath: newItem.value };
        }
        newItem["jsonPathConfig"] = newItem.value;
        break;
      case "expression":
        newItem["expression"] = newItem.value;
        break;
      case "string":
        newItem = { ...newItem, literal: { stringValue: newItem.value } };
        break;
      case "int":
        newItem = {
          ...newItem,
          literal: { intValue: parseInt(newItem.value) }
        };
        break;
      case "float":
        newItem = {
          ...newItem,
          literal: { floatValue: parseFloat(newItem.value) }
        };
        break;
      case "bool":
        newItem = {
          ...newItem,
          literal: {
            boolValue: newItem.value
              ? newItem.value.toLowerCase() === "true"
              : false
          }
        };
        break;
      default:
        break;
    }

    onChange(`${idx}`)(newItem);
  };

  const columns = [
    {
      name: "Name",
      field: "name",
      width: "30%",
      render: (name, item) => (
        <EuiFieldText
          placeholder="Name"
          value={name || ""}
          onChange={e => onChange(`${item.idx}.name`)(e.target.value)}
          isInvalid={!!get(errors, `${item.idx}.name`)}
        />
      )
    },
    {
      name: "Type",
      field: "type",
      width: "30%",
      render: (type, item) => (
        <EuiSuperSelect
          options={typeOptions}
          valueOfSelected={type || ""}
          onChange={value => onVariableChange(item.idx, "type", value)}
          isInvalid={!!get(errors, `${item.idx}.type`)}
          hasDividers
        />
      )
    },
    {
      name: "Value",
      field: "value",
      width: "30%",
      render: (value, item) => {
        if (item.type === "jsonpath") {
          return (
            <JsonPathConfigInput
              jsonPathConfig={value}
              identifier={`variables-${item.idx}`}
              onChangeHandler={val => onVariableChange(item.idx, "value", val)}
            />
          );
        }
        return (
          <EuiFieldText
            placeholder="Value"
            value={value || ""}
            onChange={e => onVariableChange(item.idx, "value", e.target.value)}
            isInvalid={!!get(errors, `${item.idx}.value`)}
          />
        );
      }
    },
    {
      width: "10%",
      actions: [
        {
          render: item =>
            item.idx < items.length - 1 ? (
              <EuiButtonIcon
                size="s"
                color="danger"
                iconType="trash"
                onClick={onDeleteVariable(item.idx)}
                aria-label="Remove variable"
              />
            ) : (
              <div />
            )
        }
      ]
    }
  ];

  const getRowProps = item => {
    const { idx } = item;
    const isInvalid = !!errors[idx];
    return {
      className: isInvalid ? "euiTableRow--isInvalid" : "",
      "data-test-subj": `row-${idx}`
    };
  };

  return (
    <InMemoryTableForm
      columns={columns}
      rowProps={getRowProps}
      items={items}
      hasActions={true}
      errors={errors}
      renderErrorHeader={key => `Row ${parseInt(key) + 1}`}
    />
  );
};
