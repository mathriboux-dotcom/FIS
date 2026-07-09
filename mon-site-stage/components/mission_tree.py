import streamlit as st
from components.data import MISSIONS

def render_mission_tree():
    with st.expander("📁 ansible", expanded=True):
        if st.button("📁 playbooks", key="playbooks_button"):
            st.session_state.page = "playbooks"
        if st.button("📁 inventories", key="inventories_button"):
            st.session_state.page = "inventories"

        with st.expander("📁 roles", expanded=False):
            if st.button("📁 fisrelay", key="fisrelay_button"):
                st.session_state.page = "fisrelay"
            if st.button("📁 fisrelay_calendar", key="fisrelay_calendar_button"):
                st.session_state.page = "fisrelay_calendar"
            if st.button("📁 fisrelay_enrichdata", key="fisrelay_enrichdata_button"):
                st.session_state.page = "fisrelay_enrichdata"
            if st.button("📁 fisrelay_load_balancing", key="fisrelay_load_balancing_button"):
                st.session_state.page = "fisrelay_load_balancing"
            if st.button("📁 fisrelay_session_chooser", key="fisrelay_session_chooser_button"):
                st.session_state.page = "fisrelay_session_chooser"

    if st.button("📁 import_conf", key="import_conf_button"):
        st.session_state.page = "import_conf"

    with st.expander("📁 scripts", expanded=False):
        if st.button("📁 build_common", key="build_common_button"):
            st.session_state.page = "build_common"
        if st.button("📁 build_sub_ini_ansible", key="build_sub_ini_ansible_button"):
            st.session_state.page = "build_sub_ini_ansible"
        if st.button("📄 restore_ini_fisrelay.sh", key="restore_ini_fisrelay_button"):
            st.session_state.page = "restore_ini_fisrelay"
        if st.button("📄 compare_common_staging_vs_production.sh", key="compare_common_button"):
            st.session_state.page = "compare_common"

    if st.button("🚀 Jenkins", key="jenkins_button"):
        st.session_state.page = "jenkins"
