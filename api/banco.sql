
--
-- Estrutura da tabela `event`
--

create table event (
  idEvent int(11) not null,
  nome varchar(200) DEFAULT NULL,
  numero int(11) not null,
  dataAcontecimento date,
  duracao int(11) not null,
  idUsuario int(11) DEFAULT NULL
)

--
-- Estrutura da tabela usuario
--

create table usuario (
  id int(11) NOT NULL,
  nome text DEFAULT NULL,
  login text DEFAULT NULL,
  email text DEFAULT NULL,
  senha text DEFAULT NULL
) 

--
-- Extraindo dados da tabela usuario
--

INSERT INTO usuario (id, nome, login, email, senha) VALUES
(1, 'Marcelo', 'marcelo', 'marcelo_xavierpaula@hotmail.com', 'marcelo123'),
(2, 'rrrrrrrrrrrrr', 'rrrrrrrrrrrrrrrrrr', 'marcelo_xavierpaula@hotmail.com', 'rrrrrrrrrrrrrrrrrrrrrrr'),
(3, '123', 'aaaaaa', 'teste@teste.com', '123456'),

--
-- Extraindo dados da tabela `event`
--

--
-- Índices para tabela `event`
--
ALTER TABLE `event`
  ADD PRIMARY KEY (`idEvent`),
  ADD KEY `idUsuario` (`idUsuario`);

--
-- Índices para tabela `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `event`
--
ALTER TABLE `event`
  MODIFY `idEvent` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de tabela `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `event`
--
ALTER TABLE `event`
  ADD CONSTRAINT `event_ibfk_1` FOREIGN KEY (`idUsuario`) REFERENCES `usuario` (`id`);
COMMIT;
