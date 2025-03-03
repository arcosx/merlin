/**
 * Copyright 2020 The Merlin Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import React from "react";
import { navigate } from "@reach/router";
import PropTypes from "prop-types";
import {
  ApplicationsContextProvider,
  CurrentProjectContextProvider,
  Header,
  ProjectsContextProvider
} from "@gojek/mlp-ui";
import config, { appConfig } from "./config";
import { EnvironmentsContextProvider } from "./providers/environments/context";

import "./PrivateLayout.scss";

export const PrivateLayout = Component => {
  return props => (
    <ApplicationsContextProvider>
      <ProjectsContextProvider>
        <CurrentProjectContextProvider {...props}>
          <Header
            homeUrl={config.HOMEPAGE}
            appIcon="machineLearningApp"
            docLinks={appConfig.docsUrl}
            onProjectSelect={projectId =>
              navigate(`${config.HOMEPAGE}/projects/${projectId}/models`)
            }
          />
          <EnvironmentsContextProvider>
            <Component {...props} />
          </EnvironmentsContextProvider>
        </CurrentProjectContextProvider>
      </ProjectsContextProvider>
    </ApplicationsContextProvider>
  );
};

PrivateLayout.propTypes = {
  projectId: PropTypes.string
};
