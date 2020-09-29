import axios from "axios";
import router from "@/router/index";

const state = {
  composes: [],
  isLoading: false
};

const mutations = {
  setComposes(state, composes) {
    state.composes = composes;
  },
  setCompose(state, compose) {
    const idx = state.composes.findIndex(x => x.id === compose.id);
    if (idx < 0) {
      state.composes.push(compose);
    } else {
      state.composes.splice(idx, 1, compose);
    }
  },
  addCompose(state, compose) {
    state.composes.push(compose);
  },
  removeCompose(state, compose) {
    const idx = state.composes.findIndex(x => x.id === compose.id);
    if (idx < 0) {
      return;
    }
    state.composes.splice(idx, 1);
  },
  setApp(state, app) {
    const idx = state.apps.findIndex(x => x.id === app.id);
    if (idx < 0) {
      state.apps.push(app);
    } else {
      state.apps.splice(idx, 1, app);
    }
  },
  setLoading(state, loading) {
    state.isLoading = loading;
  },
  setComposeVariables(state, composeVariables) {
    state.composeVariables = composeVariables;
  }
};

const actions = {
  readComposes({ commit }) {
    commit("setLoading", true);
    const url = "/api/compose/";
    axios
      .get(url)
      .then(response => {
        const composes = response.data;
        commit("setComposes", composes);
      })
      .catch(err => {
        commit("snackbar/setErr", err, { root: true });
      })
      .finally(() => {
        commit("setLoading", false);
      });
  },
  readCompose({ commit }, id) {
    commit("setLoading", true);
    const url = `/api/compose/${id}`;
    axios
      .get(url)
      .then(response => {
        const compose = response.data;
        commit("setCompose", compose);
      })
      .catch(err => {
        commit("snackbar/setErr", err, { root: true });
      })
      .finally(() => {
        commit("setLoading", false);
      });
  },
  writeCompose({ commit }, payload) {
    commit("setLoading", true);
    const url = "/api/compose/";
    axios
      .post(url, payload)
      .then(response => {
        const compose = response.data;
        commit("addCompose", compose);
      })
      .catch(err => {
        commit("snackbar/setErr", err, { root: true });
      })
      .finally(() => {
        commit("setLoading", false);
        router.push({ name: "View Composes" });
      });
  },
  updateCompose({ commit }, id) {
    commit("setLoading", true);
    const url = `/api/compose/${id}/refresh`;
    axios
      .get(url)
      .then(response => {
        const compose = response.data;
        commit("setCompose", compose);
      })
      .catch(err => {
        commit("snackbar/setErr", err, { root: true });
      })
      .finally(() => {
        commit("setLoading", false);
      });
  },
  deleteCompose({ commit }, id) {
    commit("setLoading", true);
    const url = `/api/compose/${id}`;
    axios
      .delete(url)
      .then(response => {
        const compose = response.data;
        commit("removeCompose", compose);
      })
      .catch(err => {
        commit("snackbar/setErr", err, { root: true });
      })
      .finally(() => {
        commit("setLoading", false);
      });
  },
};

const getters = {
  getComposeById(state) {
    return id => {
      return state.composes.find(x => x.id == id);
    };
  }
};

export default {
  namespaced: true,
  state,
  mutations,
  getters,
  actions
};
