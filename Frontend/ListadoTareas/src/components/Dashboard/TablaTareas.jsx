import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableContainer from "@material-ui/core/TableContainer";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import Paper from "@material-ui/core/Paper";
import { Button, makeStyles } from "@material-ui/core";
import DeleteForeverIcon from "@material-ui/icons/DeleteForever";

const useStyles = makeStyles((theme) => ({
    table: {
        minWidth: "600px",
        maxHeight: "600px",
    },
    deleteButton: {
        background: "red",
        "&:hover": {
            color: "red",
        },
    },
}));

const prioridadTarea = {
    1: "Muy baja",
    2: "Baja",
    3: "Media",
    4: "Alta",
    5: "Muy alta"
}

const TablaTareas = ({
    tareas,
    fetchTareas,
    isDeleted,
    setIsDeleted,
}) => {
    const classes = useStyles();

    async function handleDelete(idTarea) {
        await fetch(`http://localhost:8000/tareas/${idTarea}`, {
            method: "DELETE",
        });
    }
    return (
        <>
            <TableContainer component={Paper}>
                <Table className={classes.table}>
                    <TableHead>
                        <TableRow>
                            <TableCell>ID Tarea</TableCell>
                            <TableCell>Descripción tarea</TableCell>
                            <TableCell>Responsable</TableCell>
                            <TableCell>Prioridad</TableCell>
                            <TableCell align="right">Acciones</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {tareas.map( (tarea) =>
                            <TableRow key={tarea.id}>
                                <TableCell>{tarea.id}</TableCell>
                                <TableCell>{tarea.descripcion_tarea}</TableCell>
                                <TableCell>{tarea.responsable}</TableCell>
                                <TableCell>{prioridadTarea[tarea.prioridad] || "No tiene prioridad"}</TableCell>
                                <TableCell align="right">
                                    <Button
                                        className={classes.deleteButton}
                                        onClick={() => {
                                            handleDelete(
                                                tarea.id
                                            );
                                            setIsDeleted(!isDeleted);
                                        }}
                                    >
                                        <DeleteForeverIcon />
                                    </Button>
                                </TableCell>
                            </TableRow>
                            
                        )}
                    </TableBody>
                </Table>
            </TableContainer>
        </>
    );
};

export default TablaTareas;
