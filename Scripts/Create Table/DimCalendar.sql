CREATE TABLE DimCalendar (
    [Data] DATE PRIMARY KEY,
    Ano INT NOT NULL,
    Mes INT NOT NULL,
    Dia INT NOT NULL,
    DiaDaSemana VARCHAR(25) NOT NULL,
    Trimestre INT NOT NULL,
    MesAbreviado VARCHAR(5) NOT NULL
);
