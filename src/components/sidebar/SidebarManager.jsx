import React, { useEffect } from "react";
import { useState, useContext } from "react";
import { Box, IconButton, Typography, useTheme } from "@mui/material";
import { Link } from "react-router-dom";
import { tokens } from "../../style/theme";
import MenuOutlinedIcon from "@mui/icons-material/MenuOutlined";
import logo from "../../assets/smp_logo.png";
import HomeIcon from "@mui/icons-material/Home";
import AccountBoxIcon from "@mui/icons-material/AccountBox";
import HandshakeIcon from "@mui/icons-material/Handshake";
import KeyboardCommandKeyIcon from "@mui/icons-material/KeyboardCommandKey";
import {
  sidebarClasses,
  menuClasses,
  Sidebar,
  Menu,
  MenuItem,
  SubMenu,
  useProSidebar,
} from "../react-pro-sidebar";
import { Context } from "../../context/Context";

const Item = ({
    title,
    to,
    icon,
    selected,
    setSelected,
    collapsed,
  }) => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    return (
        <MenuItem
          active={selected === title}
          style={{
            color: colors.secondary[500],
          }}
          onClick={() => {
            setSelected(title);
            updateContext(title, collapsed);
          }}
          icon={icon}
          routerLink={<Link to={to} />}
        >
          <Typography>{title}</Typography>
        </MenuItem>
      );
    };

const Sidebar_ = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);
    const [selected, setSelected] = useState(context.appState.sidebar.page);      
    const { toggleSidebar, collapseSidebar, broken, rtl, collapsed } =
        useProSidebar();

    function updateContext(title, state) {
        context.setAppState({
            ...context.appState,
            sidebar: {
            page: title,
            collapsed: state,
            },
        });
    }

    return (
        <Box
            style={{
            display: "flex",
            height: "100vh",
            direction: rtl ? "rtl" : "ltr",
        }}
        >
        <Sidebar
            breakPoint="lg"
            rootStyles={{
            [`.${sidebarClasses.container}`]: {
                backgroundColor: `${colors.accent4[600]} !important`,
            },
            [`.${menuClasses.subMenuContent}`]: {
                backgroundColor: `${colors.accent4[600]} !important`,
            },
            }}
        >
        <Box>
            <Menu
                menuItemStyles={{
                button: ({ level, active, disabled, isSubmenu }) => {
                    if (level === 0)
                    return {
                        // color: disabled ? "#f5d9ff" : "#d359ff",
                        backgroundColor: active
                        ? `${colors.accent4[500]}`
                        : undefined,
                    };
                },
                }}
                >
                  {/* LOGO AND MENU ICON */}
                  {!collapsed ? (
                    <Box
                      height={"60px"}
                      width={"100%"}
                      display={"flex"}
                      justifyContent={"space-evenly"}
                      paddingTop={"10px"}
                    >
                      <img src={logo} alt="logo" />
                    </Box>
                  ) : (
                    <Box
                      height={"50px"}
                      width={"100%"}
                      display={"flex"}
                      justifyContent={"space-around"}
                      paddingTop={"10px"}
                    >
                      <img src={logo} alt="logo" />
                    </Box>
                  )}
                  {!collapsed && broken ? (
                    <Box display="flex" justifyContent="center" alignItems="center">
                      <IconButton
                        className="sb-button"
                        onClick={() => collapseSidebar()}
                      >
                        <MenuOutlinedIcon />
                      </IconButton>
                    </Box>
                  ) : (
                    broken && (
                      <Box display="flex" justifyContent="center" alignItems="center">
                        <IconButton
                          className="sb-button"
                          onClick={() => collapseSidebar()}
                        >
                          <MenuOutlinedIcon />
                        </IconButton>
                      </Box>
                    )
                  )}
                  <br />
                  
                  <Item
                    title="Home"
                    to={`/manager/home`}
                    icon={<HomeIcon />}
                    selected={selected}
                    setSelected={setSelected}
                    updateContext={updateContext}
                    collapsed={collapsed}
                  />
                </Menu>
              </Box>
            </Sidebar>
          </Box>
        );
      };
      
      export default Sidebar_;
      