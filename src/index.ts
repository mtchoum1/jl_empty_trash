import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { requestAPI } from './handler';

/**
 * Initialization data for the jl_empty_trash extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'jl_empty_trash:plugin',
  description: 'Empty Trash extension for jupyter lab',
  autoStart: true,
  activate: (app: JupyterFrontEnd) => {
    console.log('JupyterLab extension jl_empty_trash is activated!');

    requestAPI<any>('get-example')
      .then(data => {
        console.log(data);
      })
      .catch(reason => {
        console.error(
          `The jl_empty_trash server extension appears to be missing.\n${reason}`
        );
      });
  }
};

export default plugin;
