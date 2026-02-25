import { Grid, Typography, createTheme, makeStyles } from "@material-ui/core";
import { purple } from "@material-ui/core/colors";
import { useEffect, useState } from "react";
import TablaTareas from "./TablaTareas";

const theme = createTheme({
    palette: {
        primary: purple,
    },
});

const useStyles = makeStyles((theme) => ({
    root: {
        marginTop: "60px",
        height: "100vh",
        display: "flex",
        backgroundColor: "#f5f5f5",
        justifyContent: "center",
        alignItems: "center",
        textAlign: "center",
    },
    container: {
        maxWidth: "85%",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        flexDirection: "column",
        "& > *": {
            margin: "10px",
        },
    },
    title: {
        [theme.breakpoints.down("sm")]: {
            fontSize: "24px",
        },
    },
    titleStyles: {
        color: "#802c6e",
    },
}));

const Dashboard = () => {
    const classes = useStyles();
    const [tareas, setTareas] = useState();
    const [isDeleted, setIsDeleted] = useState(false);
    const fetchTareas = () => {
        fetch("http://localhost:8000/tareas/")
            .then((response) => response.json())
            .then((data) => {
                setTareas(data);
            });
    };
    useEffect(() => {
        fetchTareas();
    }, [isDeleted]);
    return (
        <>
            <Grid container className={classes.root}>
                <div className={classes.container}>
                    <Typography variant="h4" className={classes.title}>
                        Bienvenido al{" "}
                        <span className={classes.titleStyles}>
                            Listado de Tareas
                        </span>
                        , acá podrá ver una lista de facturas con una serie de
                        opciones, en las cuales usted decide qué hacer.
                        {tareas && (
                            <TablaTareas
                                tareas={tareas}
                                fetchTareas={fetchTareas}
                                isDeleted={isDeleted}
                                setIsDeleted={setIsDeleted}
                            />
                        )}
                    </Typography>
                </div>
            </Grid>
        </>
    );
};

export default Dashboard;
